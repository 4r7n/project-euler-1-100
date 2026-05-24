t = 0
for x in range(1, 50):
    for n in range(1, 50):
        if len(str(x**n))==n:
            t += 1
            print(x, n)