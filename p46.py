import math

def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]

primes = eratos(10000)
lookup = set(primes)

squares = [2*i**2 for i in range(1, 1230)]


def valid(n):
    found = False
    i = 0

    sq = set(squares[:math.ceil((n/2)**0.5)])

    while not found:
        if primes[i]>n:
            return n

        if (n-primes[i]) in sq:
            return False

        i+=1


composite = [i for i in range(3, 10000, 2) if i not in lookup]


for i in composite:
    if valid(i)!=False:
        print(i)
        break