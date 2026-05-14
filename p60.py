__import__("sys").setrecursionlimit(10000)

def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]

lookup = set(eratos(90000000))
primes = eratos(10000)

def valid(s):
    return all([int(str(a) + str(b)) in lookup for a in s for b in s if not a==b])


def expand(S):
    return tuple(p for p in primes if p not in set(S) and valid(S + tuple([p])))

visited = set()

def search(Q = tuple()):
    visited.add(tuple(sorted(Q)))
    N = expand(Q)

    if len(Q)==5:
        return Q

    elif N == tuple():
        return search(Q[:-1])

    else:
        for n in N:
            t = Q+tuple([n])

            if tuple(sorted(t)) not in visited:
                return search(t)

        if Q==tuple():
            return None

        return search(Q[:-1])

print(sum(search()))