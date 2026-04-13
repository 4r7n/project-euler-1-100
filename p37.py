def eratos(n):
    sieve = bytearray([1]) * (n+1)  #p27 for more context
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return set([i for i in range(n+1) if sieve[i]])

count = 4

eratosthene = eratos(10**7)

search = sorted([i for i in eratosthene if (int(str(i)[0]) in eratosthene) and (int(str(i)[-1]) in eratosthene)]) #pruning

found = set()

while len(found)<11:

    valid = True
    check = str(search[count])

    for i in range(1, len(check)):
        if (int(check[i:]) not in eratosthene) or (int(check[:-i]) not in eratosthene):
            valid = False
            break

    if valid:
        found.add(search[count])

    count += 1

print(sum(found))