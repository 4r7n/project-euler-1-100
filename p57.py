cache = {-1: [1, 0], 0: [1, 1]}

#https://en.wikipedia.org/wiki/Continued_fraction#Formulation
def conv(n):
    if n in cache:
        return cache[n]

    p1, q1 = conv(n-1)
    p2, q2 = conv(n-2)

    res = [2*p1 + p2,
           2*q1 + q2]


    cache[n] = res
    return res

print(sum([len(str(conv(i)[0]))>len(str(conv(i)[1])) for i in range(1000)]))