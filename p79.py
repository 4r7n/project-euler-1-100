attempts = [rl.strip("\n") for rl in open("p79_keylog.txt", "r")]
#read in the file

distinct = set("".join(attempts))
D = dict(zip(distinct, [set() for l in range(len(distinct))]))
#find all the distinct digits, this will be length of the password
#we also assign each variable a set

for A in attempts:
    for i, it in enumerate(A):

        for j in range(2-i):
            D[it].add(A[j+1+i])

        #for each value in the attempt, we track which values appear are greater than itself
        #this means that, by the end each value will have a distinct number of values greater than itself

P = ["hi" for l in range(len(distinct))]

for k in D.keys():
    P[len(D[k])] = k
    #the amount of values greater than itself defines each key's position

print("".join(P[::-1]))
#because we stored greater values, we have to reverse the order!