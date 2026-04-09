import math

def factor(n, x):
    return n % x == 0

def divisors(n):  #this copied from my p12, so check there for more context if needed
    d = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if factor(n, i):
            d.append(int(n/i))
            d.append(i)

    d = list(set(d))

    return sum(filter((lambda x: x<n), d)) #however this time we and filter out any numbers greater than n, then return the sum of those numbers

ambicable = []

check = [i for i in range(1, 10000)] #the numbers we need to check

while not check==[]:
    if divisors(check[0])==check[0]:
        check.remove(check[0])  # a =/= b
        #we remove each number we check

    elif check[0]==divisors(divisors(check[0])):
        ambicable+=[check[0], divisors(check[0])]  #if we found a pair, add it to the list and remove the number we checked from the search!

    check.remove(check[0])
    #we stop checking the number regardless


print(sum(set((ambicable)))) #print the sum of the non duplicated ambicable numbers