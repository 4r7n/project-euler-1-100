from math import log

with open("p99_base_exp.txt", "r") as f:
    rl = f.readlines()

rl = [tuple(map(int, i.strip().split(","))) for i in rl]
m = 0
L = 0

for l, pwr in enumerate(rl):
    n = pwr[1]*log(pwr[0])

    if n>m:
        m = n
        L = l

print(L+1)