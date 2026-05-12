E = [1 if i % 3 else 2*(i//3) for i in range(1, 101)]

cache = {-1: [1, 0], 0: [2, 1]}

#https://en.wikipedia.org/wiki/Continued_fraction#Formulation
def conv(n):
    if n in cache:
        return cache[n]

    p1, q1 = conv(n-1)
    p2, q2 = conv(n-2)

    res = [E[n]*p1 + p2,
           E[n]*q1 + q2]


    cache[n] = res
    return res

print(sum([int(s) for s in str(conv(99)[0])]))