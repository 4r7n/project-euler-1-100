F = list(map(int, open("p59_cipher.txt").read().split(",")))

k = [97, 97, 97]

def decrypt(F, k):
    return [c ^ k[i % 3] for i, c in enumerate(F)]

while True:
    D = decrypt(F, k)

    if all(32 <= c < 127 for c in D):
        T = "".join(map(chr, D))

        if " the " in T:
            print(T)

            print("\n", sum(D))
            break

    k[2] += 1

    if k[2] == 123:
        k[2] = 97
        k[1] += 1

    if k[1] == 123:
        k[1] = 97
        k[0] += 1