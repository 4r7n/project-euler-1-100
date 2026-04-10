import math

def factor(n, x):
    return n % x == 0

def isPrime(n):
    if n in [1, 2]:
        return bool(-1 + n)

    for i in range(2, int(math.sqrt(n)) + 1):
        if factor(n, i):
            return False

    return True


#multiples of 2 and 5 have the same amount of recurring digits, also the number will be a prime number as factors will share its recurrence properties
scope = [i for i in range(1, 1000) if not(factor(i, 2) or factor(i, 5)) and isPrime(i)]



count = 1

while not len(scope)==1:   #7 is a factor of 999999 and its recurring trail is of length 6 (142857), so we can eliminate everythiing from the scope of possible numbers
    scope = [i for i in scope if not factor(int("9"*count), i)]
    count+=1   #1 by one until the greatest one remains


print(scope.pop())