n = 100

smsq = sum([i**2 for i in range(1, n+1)]) #sum of squares to n, create a list of the square numbers to n, then sum them

sqsm = sum([i for i in range(1, n+1)])**2 #square of sums, sum up all the numbers to n, then square that number

print(sqsm-smsq) #take the difference of both numbers
