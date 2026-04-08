import math

def triangle(n, l=[1]): #parameter l, so we can generate further, rather that starting from a blank slte

    for i in range(n-1):
        l.append(l[-1]+len(l)+1)

    return l   #returns a list of length l triangle numbers from 1, we can determine the next number by taking the last number and adding the lenght of the list +1 which would be the next number of the sequence


def factor(n, x):
    return n % x == 0


def divisors(n):
    d = [] #we will use this as a counter for every number divisble
    for i in range(1, int(math.sqrt(n)) + 1):
        if factor(n, i):
            d.append(int(n/i))
            d.append(i)  #for every factor, we increment d by both factors, as we are checking if n is a factor of i, this means there are two factors, and we can add

            #as we are checking both ways, we only need to go up to the square root, making it more efficient

    d = list(set(d)) #this removes any duplicates

    return len(d)


tri = triangle(5000) # starting list, we can add more later if needed
maxDivisors = 0
c = -1 #(count)

while maxDivisors<500:
    c+=1

    if c==len(tri)-1:
        tri = triangle(5000, tri) #if we run out of triangle numbers, find the next 5000

    if divisors(tri[c])>maxDivisors:
        maxDivisors = divisors(tri[c])

print(tri[c]) #the loop will break when the divisors of a number exceed 500, then we can output tri[c], the number we just checked