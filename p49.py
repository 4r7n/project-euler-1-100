from itertools import permutations

def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]


primes = [i for i in eratos(10000) if i>999]
s = set(primes)

sequences = []

for p in primes:
    perm = [i-p for i in sorted(list(set([int("".join(i)) for i in permutations(str(p)) if int("".join(i)) in s])))]

    if len(perm)>2:
        for i in perm[1:]:
            if 2*i in perm and i>0:
                sequences.append(str(p)+str(i+p)+str(2*i+p))

print(sequences[1])