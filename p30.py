#we dont need to check numbers greater than 999999, because f(9999999) = 7*(9^5) = 313343, which is not seven digits

print(sum(set(n for n in range(2, 1000000) if n==sum([int(i)**5 for i in str(n)]))))  # we can test for numbers by turning them to a string then iterate over it by treating the iter as an int
