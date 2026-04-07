(lambda ln: ([a:=[]]+list(filter(lambda x: False if x==None else True, [(lambda l: l.append(1) if l==[1] or l==[] else l.append(l[-1]+l[-2]))(a) for item in range(ln)])))[0]) #funny one line fibonacci i made (we dont need it)

def fibonacci(limit):
    if limit<1:
        return [] #to prevent any unwarranted errors

    else:
        fib = [1, 1]

        while (fib[-1]+fib[-2])<=limit:
            fib.append(fib[-1]+fib[-2])

        return fib

        #add previous two terms of list until the current term exceeds the limit
        #then return the list


print(sum([i for i in fibonacci(4000000) if i%2==0]))

#generate the list of fibonacci numbers which dont exceed four million, via the function we created
#only keep the even values, and return the sum
