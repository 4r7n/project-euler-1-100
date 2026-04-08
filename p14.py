def collatz(n):
    steps = 1 #as shown in the question, the size of the chain includes itself

    while not n == 1: #while n is not equal to 1
        steps += 1

        if n%2==0: #if n is even  (or more technically, if the remainder of n when divided by two is zero: )
            n = n // 2

        else:
            n = 3*n + 1

    return steps


maxCollatz = [0, 0]

for i in range(1, 1000000):
    if collatz(i)>maxCollatz[1]:
        maxCollatz = [i, collatz(i)] #checking for a greater value, but we also store the value that produces it

print(maxCollatz[0])