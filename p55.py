cache = {}

def search(n, c = 0):
    n = n + int(str(n)[::-1])

    if n in cache:
        return cache[n]

    elif str(n)==str(n)[::-1]:
        return 0

    elif c > 50:
        return 1

    res = search(n, c + 1)
    cache[n] = res

    return res

print(sum(map(search, range(1, 10**4))))