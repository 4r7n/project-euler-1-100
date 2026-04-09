#this one is a brief one haha

print(sum(map(int, list(str((lambda n: ([x:=1]*0 + [x:=i*x for i in range(1, n+1)])[-1])(100))))))



