from math import isqrt, sqrt, floor

def period_sqrt(n):
    a0 = isqrt(n)
    m, d, a = 0, 1, a0

    seen = {}
    seq = []

    for i in range(1000):
        state = (m, d, a)
        if state in seen:
            return (i - seen[state])%2

        seen[state] = i
        seq.append(a)

        m = d*a - m
        d = (n - m*m) // d
        a = (a0 + m) // d


Q = set(i**2 for i in range(100))
print(sum(period_sqrt(i) for i in range(2, 10000) if not i in Q))