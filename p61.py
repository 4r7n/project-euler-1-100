tri = set(int(0.5*((n**2) + n)) for n in range(1, 10000))
sq = set(n**2 for n in range(1, 10000))
penta = set(int(0.5*(3*(n**2) - n)) for n in range(1, 10000))
hexa = set(int(2*(n**2) - n) for n in range(1, 10000))
hepta = set(int(0.5*(5*(n**2) - 3*n)) for n in range(1, 10000))
octa = set(int(3*(n**2) - 2*n) for n in range(1, 10000))

L = [tri, sq, penta, hexa, hepta, octa]

for q, SeT in enumerate(L):
    L[q] = [S for S in SeT if len(str(S))==4]


def expand(v, N):
    for n in N:
        for s in map(str, L[n]):
            if v[2:] == s[:2]:
                yield s, n


def check(v, N = [0, 1, 2, 3, 4], R = []):
    if N == []:
        return sum(R) if str(R[0])[:2] == str(R[-1])[2:] else None

    for Q, d in expand(v, N):
        R.append(int(Q))

        r = check(Q, N = [n for n in N if n != d], R = R)

        if r is not None:
            return r

        R.pop()

    return None


for o in L[5]:
    c = check(str(o), R = [o])
    if c is not None:
        print(c)