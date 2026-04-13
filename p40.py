print((lambda x: ([l:=1] + [l := l * int(x[10**i - 1]) for i in range(0, 7)])[-1])("".join([str(i) for i in range(1, 200000)])))
