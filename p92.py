cache = {1: 0, 89: 1} #if n is 1 or 89, we can say its true / false

def step(n):
    if n in cache:
        return cache[n]

    Next = sum(int(s)**2 for s in str(n)) #iterate through the number as if it were a string then square each digit and add them all up

    res = step(Next)  #call the function with the next number, until we reach 1 or 89

    cache[n] = res  #this way all the numbers in the process will be marked as true or false, so the next time we reach this number in any chain, we can instantly deduce it and all numbers before.

    return res


total = 0
for i in range(1, 10000000):   #check all numbers up to 10 million, and keep track
    total += step(i)

print(total)