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

[final, count, found] = [10001, 0, 0]

while not (found==final): #honestly, this is a bit of a lazy solution, but the number is small enough and im in a bit of a rush!
    count+=1                 #essentially, we just keep iterating through the natural numbers and keeping track of when we encounter a prime number
    if isPrime(count):       #the loop ends when we reach final, and we can output the current number (count)
        found+=1

print(count)