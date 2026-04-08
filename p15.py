size = 20
paths = [] #this question is a little trickier, we are going to use memoization to traverse the paths

#the reason we need memoization rather than straight recursion is that the answer is extremely large, but we can approach it in a recurisve way, as a lot of the calculations are being used more than once


directions = {
"d": lambda coords: (coords[0], coords[1]+1),
"r": lambda coords: (coords[0]+1, coords[1])  #a dictionary to simulate the coordinates moving left and right
}

cache = {} #this will be our cache, and it will tell us how many path pass through the point

def search(cd=(0, 0)):
    if cd==(size, size):
        return 1 #if we are finish we add one path

    if cd in cache:
        return cache[cd] #if we have already calculated this point before, we can return its value

    elif cd[0]==size:
        res = search(directions["d"](cd))  #else if we are at 20 at each side, we can only move in one direction

    elif cd[1]==size:
        res = search(directions["r"](cd))

    else:
        res = search(directions["d"](cd)) + search(directions["r"](cd)) #otherwise, we will simulate going down and right

    cache[cd] = res #and add the paths from the point to our cache
    return res


print(search())