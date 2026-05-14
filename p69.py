def sieve(n):
    phi = list(range(n + 1))

    for p in range(2, n + 1):
        if phi[p] == p:
            for j in range(p, n + 1, p):
                phi[j] -= phi[j] // p

    return phi


S = [i/it for i, it in enumerate(sieve(1000001)) if not i==0]
print(S.index(max(S)) + 1)