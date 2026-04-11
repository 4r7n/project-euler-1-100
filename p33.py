import math

frac = set()

for a in range(11, 100):
    for b in range(11, 100):
        if not(b%10 == 0 or b<a or len(set(str(a)+str(b)))!=3 ):
            if str(a)[0]==str(b)[0]:
                if a/b == int(str(a)[1])/int(str(b)[1]):
                    frac.add((a, b))
            elif str(a)[0]==str(b)[1]:
                if a/b == int(str(a)[1])/int(str(b)[0]):
                    frac.add((a, b))
            elif str(a)[1]==str(b)[1]:
                if a/b == int(str(a)[0])/int(str(b)[0]):
                    frac.add((a, b))
            elif str(a)[1]==str(b)[0]:
                if a/b == int(str(a)[0])/int(str(b)[1]):
                    frac.add((a, b))

print(int(1 / (math.prod([i[0] for i in frac]) / math.prod([j[1] for j in frac]))))