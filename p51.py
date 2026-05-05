import itertools

def eratos(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])

    return [i for i in range(n+1) if sieve[i]]

primes = eratos(1000000)
lookup = set(primes)


def replac(n, rep):
    k, c = list(str(n)), []
    rep = set(rep)

    for j in range(0, 10):
        if k[0] in rep and j == 0:
            continue

        r = int("".join([str(j) if i in rep else it for i, it in enumerate(k)]))
        if r in lookup:
            c.append(r)


    return c


def checks(n):
    a = (itertools.product("10",repeat=n))
    return list(set(tuple(i for i, it in enumerate(j) if it=="1") for j in a))



for n in range(6):
    for check in checks(n):

        if not check==():

            for item in [p for p in primes if len(str(p))==n+1]:
                r = replac(item, check)

                if len(r)==8:
                    if len(str(min(r)))==n+1:
                        print(min(r))

                    break