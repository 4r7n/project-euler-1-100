from math import comb

c = 0
for n in range(1, 101):
    for r in range(n):
        if comb(n, r)>1000000:
            c+=1

print(c)