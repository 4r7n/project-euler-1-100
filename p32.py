def pandigital(a, b):
    if "".join(sorted(str(a)+str(b)+str(a*b)))=="123456789":
        return a*b
    return 0


pd9 = set()

for a in range(0, 2000):
    for b in range(0, 1000):
        pd9.add(pandigital(a, b))

print(sum(pd9))