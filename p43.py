from itertools import permutations

def valid(n):
    if int(n[1]+n[2]+n[3])%2==0:
        if int(n[2]+n[3]+n[4])%3==0:
            if int(n[3]+n[4]+n[5])%5==0:
                if int(n[4]+n[5]+n[6])%7==0:
                    if int(n[5]+n[6]+n[7])%11==0:
                        if int(n[6]+n[7]+n[8])%13==0:
                            if int(n[7]+n[8]+n[9])%17==0:
                                return True
    return False


print(sum([int("".join(i)) for i in set(permutations("0123456789")) if valid(i)]))