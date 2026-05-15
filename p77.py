def Sieve(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]


primes = Sieve(100)
mx = len(primes)

cache = {}


def comb(n = 0, target = 0):
    if (n, target) in cache:
        return cache[(n, target)]

    if target==0:
        cache[(n, target)] = 1
        return 1

    if target<0:
        cache[(n, target)] = 0
        return 0

    if n>=mx:
        cache[(n, target)] = 0
        return 0

    res = comb(n, target - primes[n]) +  comb(n + 1, target)
    cache[(n, target)] = res

    return res


def ps(n):
    return comb(0, n)

c, C = 0, 5000

while True:
    sol = ps(c)
    if sol>=C:
        print(c)
        break

    else:
        c += 1