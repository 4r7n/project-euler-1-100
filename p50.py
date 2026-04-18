def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]


primes = eratos(1000000)
s = set(primes)


d = 1

def search():
    for size in range(len(primes), 1, -1):
        for i in range(len(primes) - size):
            sm = sum(primes[i: size+i])

            if sm>1000000:
                break

            if sm in s:
                return sm


print(search())