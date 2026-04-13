solutions = [0 for i in range(1, 1001)]

found = set()

for a in range(1, 500):
    for b in range(1, 500):
        c = ((a**2 + b**2)**0.5)

        if c.is_integer():
            found.add(tuple(sorted((a, b, int(c)))))

for k in [sum(i) for i in list(found) if sum(i)<=1000]:
    solutions[k-1] += 1

print(solutions.index(max(solutions))+1)