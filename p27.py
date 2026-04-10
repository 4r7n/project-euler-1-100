def isPrime(n):
    if n in range(0, 4) or n < 0:
        return n > 1

    if n % 3 == 0 or n % 2 == 0:
        return False

    i = 5

    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False

        i += 6

    return True   #i made a more efficient prime checker, the main take away is we instantly deduce multiples of 3 and 2
                  #therefore letting us start at 5 and also being able to iterate every six, as we check two greater than the number in the same instance


def evalQuad(a, b):
    end, consec = False, 0

    while not end:
        if isPrime((consec**2) + (a*consec) + b):  #we can evaluate quadratics, by just checking them until they dont produce a prime, and return how many they produced
            consec += 1

        else:
            end = True

    return consec # i could use the sieve for more efficient eval quad implementing, but i made it b4 the sieve and for this q its unessecary


def sieve(n):
    sieve = bytearray([1]) * (n+1)  #this is eratosthenes' sieve, it works by assuming every prime up to n is true,
    sieve[0:2] = b'\x00\x00'        #then checking every multiple in the list, and crossing off ones, that are divisble, this can be optimising by checking up sqrt(i) and skipping multiples of 2

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])   #this is useful for the question, as we start from zero, (n^2 + an) = 0, so must b must be prime

    return [i for i in range(n+1) if sieve[i]]


maxC = [0, 0]
for a in range(-999, 1000):
    for b in sieve(1000):
        primes = evalQuad(a, b)

        if primes>maxC[0]:  #just checking which yields the greatest
            maxC[0] = primes
            maxC[1] = a*b

print(maxC[1])

