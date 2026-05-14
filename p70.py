def sieve(n):
    phi = list(range(n + 1))

    for p in range(2, n + 1):
        if phi[p] == p:
            for j in range(p, n + 1, p):
                phi[j] -= phi[j] // p

    return phi[1:]

def perm(a, b):
    return sorted(str(a))==sorted(str(b)) and not(a==b)

T = sieve(10**7)

S = [(a/b, a) for a, b in enumerate(T, start=1) if perm(a, b)]
print(min(S)[1])