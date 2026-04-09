tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

tri = [list(map(int, n.split(" "))) for n in tri.split("\n")]  #lets firstly make our triangle into a list

cache = {} #we are going to be using memoisation, because it is good

def search(row=0, col=0):

    if row==len(tri)-1:
        return tri[row][col]  #we will traverse through each row and column, the base case, is the final position at the bottom of the triangle

    if (row, col) in cache:
        return cache[(row, col)]  #if we have already cached it, we can use it

    res = tri[row][col] + max(search(row+1, col), search(row+1, col+1))  #we can use max, to find which side yeilds the greater sum, then add it to the cache
    cache[(row, col)] = res

    return res #the final call will return the greatest sum, as we work backwards to the top, we need to return the result recusively too

print(search())