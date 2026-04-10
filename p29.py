terms = set()

for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b)  #this one abuses that computers are fast...

#print(len(terms), but here is a one line implementation
print(len(set(a**b for a in range(2, 101) for b in range(2, 101))))