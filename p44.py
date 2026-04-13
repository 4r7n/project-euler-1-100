lookup = set(int(0.5*(3*(n**2) - n)) for n in range(1, 50000))

penta = [int(0.5*(3*(n**2) - n)) for n in range(1, 2500)]

for a in penta:
    for b in penta:
        if (a+b in lookup) and (a-b in lookup):
            search = (a, b)
            break

print(min(abs(search[0]-search[1]), abs(search[1]-search[0])))