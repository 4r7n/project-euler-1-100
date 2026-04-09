#cheeky recursion
import sys

sys.setrecursionlimit(4800)


def f1000(n = 1000, l = [1, 1]):
    l.append(l[-2]+l[-1])

    if len(str(l[-1]))>=n:
        return l.index(l[-1])+1

    else:
        return f1000(n, l)

print(f1000())