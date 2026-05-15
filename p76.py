order = {k: k+1 for k in range(100)}

cache = {}
value = 99

def comb(n = 0, target = order[value]):
    if (n, target) in cache:
        return cache[(n, target)]

    if target==0:
        cache[(n, target)] = 1
        return 1

    if target<0:
        cache[(n, target)] = 0
        return 0

    if n>=value:
        cache[(n, target)] = 0
        return 0

    res = comb(n, target - order[n]) +  comb(n + 1, target)
    cache[(n, target)] = res

    return res

print(comb())