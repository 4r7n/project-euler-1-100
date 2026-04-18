def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]

primes = eratos(500000)
lookup = set(primes)

def factors(n):
    f, i = 0, 0

    c = n

    while True:
        if primes[i]>c:
            return f

        if n%primes[i]==0:
            f+=1

            c = c // primes[i]

            if f>4:
                return 0

        i+=1


c, streak = 1, 0

while True:
    if factors(c)==4:
        streak+=1

    else:
        streak = 0

    if streak==4:
        print(c-3)
        break

    c+=1