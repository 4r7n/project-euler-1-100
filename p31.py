order = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50, 6: 100, 7: 200}  #values of each coin

cache = {}
value = 7

def comb(n = 0, target = order[value]):
    if (n, target) in cache:
        return cache[(n, target)]  #this is a memoised function so, we store results for efficiency

    if target==0:
        cache[(n, target)] = 1  #if we reached our target, using the coins, then it is possible using coins {n}
        return 1

    if target<0:
        cache[(n, target)] = 0  #if using another coin, exceeds the target
        return 0

    if n>value:
        cache[(n, target)] = 0  #...or runs out of coins, then both ways are impossible
        return 0

    res = comb(n, target - order[n]) +  comb(n + 1, target) #then we simulate taking a coin + losing a coin
    cache[(n, target)] = res

    return res

print(comb())