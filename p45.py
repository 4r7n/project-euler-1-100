tri = [int(0.5*((n**2) + n)) for n in range(1, 100000)]
penta = set(int(0.5*(3*(n**2) - n)) for n in range(1, 200000))
hexa = set(int(2*(n**2) - n) for n in range(1, 200000))

found, count = [], 0

while len(found)<2:
    count += 1

    check = tri[count]
    if (check in penta) and (check in hexa):
        found.append(check)

print(check)