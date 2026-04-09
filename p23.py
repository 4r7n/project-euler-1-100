import math

def factor(n, x):
    return n % x == 0

def divisors(n):
    d = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if factor(n, i):
            d.append(int(n/i))
            d.append(i)

    d = list(set(d))

    return sum(filter((lambda x: x<n), d))


abundant = [i for i in range(1, 28124) if divisors(i)>i]

cache = set()

for x in abundant:
    for y in abundant:
        if (x + y)<28124:
            cache.add(x + y)

print(sum([i for i in range(1, 28124) if i not in cache]))