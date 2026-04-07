import math #for square root

def factor(n, x):
    return n % x == 0

def isPrime(n):  #functions that check for primes and factors, see p3 if more context needed
    if n in [1, 2]:
        return bool(-1 + n)

    for i in range(2, int(math.sqrt(n)) + 1):
        if factor(n, i):
            return False

    return True

#very similar to p7

count = 0
primes = [0] #0 is not a prime, but im adding it to the list to not cause an error
limit = 2000000

while (primes[-1]<limit):
    count+=1
    if isPrime(count):
        primes.append(count)  #keep adding primes we find to the list, until one is too large

print(sum(primes[:-1])) #sum, but without the final prime