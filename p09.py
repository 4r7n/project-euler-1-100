def pythag(a, b, c):
    return (a**2+b**2==c**2)

    #func to determine if a, b, c is pythagorean

# as a+b+c == 1000, we know none of them exceed 998

squares = [i**2 for i in range(1, 1000)] #1000 for good measure haha

#as we are dealing with only square numbers, we can check if a+b is in squares, (as in a and b are also in squares)
#we wont need sqrt, as we can just use the index of the squared number in squares!

triples = [map(lambda x: x+1, [squares.index(a), squares.index(b), squares.index(a+b)]) for a in squares for b in squares if (a+b) in squares] #create a list of a, b, c where conditions for pythagorean triple is satisfied

triples = [list(i) for i in triples]

def product(l):
    r = 1
    for x in l:
        r *= x
    return r #product of a list, see p8 for more context

print(set([product(i) for i in triples if sum(i)==1000]).pop()) #return the product of the value in triples, that the sum is 1000, set to remove the dupe


