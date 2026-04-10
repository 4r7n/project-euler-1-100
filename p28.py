def spiral(n):
    if n == 1:
        return [1]


    prev = spiral(n - 2)
    start = prev[-1] + 1

    l = []

    for i in range(8 * (n//2)):    #by analysing the spirals, i found some mathematic facts, for consecutive odd integers z**2 - y**2 = 8*(z//2)
                                 # for example, 25 - 9 = 16, 5//2 = 2, 2*8 = 16, and follows for all numbers
        if i % (2 * (n//2)) == 0:  #secondly, is that the diagonal numbers fall on every (2 * (n//2))th, number in ring[n]'s layer of spiral when we start from a corner
            l.append(n**2 - i)   #i implemented it recursively, by setting the base case as n = 1: [1], then keeping track of the corners and building upon the ring


    return prev + l

print(sum(spiral(1001)))