from math import factorial

cache = {}

def fct(n):
    if n in cache:
        return cache[n]

    cache[n] = sum(factorial(int(i)) for i in str(n))
    return cache[n]



def conv(n, S = set()):
    if n in S:
        if len(S)==60:
            return 1

        return 0

    S.add(n)


    res = conv(fct(n), S)
    return res

t = 0
if True:
    for i in range(1, 1_000_000):
        if conv(i, set()):
            t+=1

print(t)