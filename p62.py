C = set(i**3 for i in range(10000))
L = sorted(C)

def perm(C, k):
    return set(n for n in C if (len(k)==len(str(n))) and sorted(k)==sorted(str(n)))

found = False


while not found:
    O = perm(C, str(L[0]))

    if len(O)==5:
        print(min(O))
        break

    for item in O:
        C.remove(item)
        L.remove(item)