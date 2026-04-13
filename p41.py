def eratos(n):
    sieve = bytearray([1]) * (n+1)  #p27 for more context
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return set([i for i in range(n+1) if sieve[i]])


def pandigital(n):
    return [str(i) for i in range(1, len(str(n))+1)] == sorted(str(n))


search = [i for i in eratos(10000000) if pandigital(i)]

print(max(search))