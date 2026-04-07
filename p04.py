def palindrome(n):
    return str(n)==str(n)[::-1] #is n equivalent to the reverse of itself?


print(max([i*j for j in range(100, 1000) for i in range(100, 1000) if palindrome(i*j)]))  #create a list of values from i and j 100->999, i*j, only keep the values where i*j is a palindrome, then return the maximum value
