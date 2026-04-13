def concatPandigital(k):
    pand = ""
    n = 1

    while len(pand)<9:
        pand += str(k*n)
        n += 1

    return ["".join(sorted(pand))=="123456789", int(pand)]

maxP = 0

for i in range(1, 100000):
    query = concatPandigital(i)
    if query[0] and query[1]>maxP:
        maxP = query[1]

print(maxP)