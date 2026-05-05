from itertools import permutations

def valid(n):
    p = set(int("".join(i)) for i in permutations(str(n)))

    if (n in p) and (2*n in p) and (3*n in p) and (4*n in p) and (5*n in p) and (6*n in p):
        return n

[c, Found] = [1, False]

while not Found:
    if valid(c):

        print(c)
        Found = True

    c+=1