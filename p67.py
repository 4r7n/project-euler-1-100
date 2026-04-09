with open("p67_triangle.txt", "r") as f: #identical to p18, apart from reading the file, check there for more context
    tri = f.read()

tri = [list(map(int, n.split(" "))) for n in tri.split("\n")]

cache = {}
a = 0

def search(row=0, col=0):
    global a
    a+=1

    if row==len(tri)-1:
        return tri[row][col]

    if (row, col) in cache:
        return cache[(row, col)]

    res = tri[row][col] + max(search(row+1, col), search(row+1, col+1))
    cache[(row, col)] = res

    return res

print(search(), a)