partitions = [1]
n = 1

while True:
    total = 0
    k = 1

    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2

        if g1 > n:
            break

        sign = -1 if k % 2 == 0 else 1

        total += sign * partitions[n - g1]

        if g2 <= n:
            total += sign * partitions[n - g2]

        k += 1

    total %= 1000000
    partitions.append(total)

    if total == 0:
        print(n)
        break

    n += 1