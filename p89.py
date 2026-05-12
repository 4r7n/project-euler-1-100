def minimal(n):
    R = {
        1:     "I",
        4:    "IV",
        5:     "V",
        9:    "IX",
        10:    "X",
        40:   "XL",
        50:    "L",
        90:   "XC",
        100:   "C",
        400:  "CD",
        500:   "D",
        900:  "CM",
        1000:  "M",
    }

    st = ""

    while n>0:

        for item in reversed(R.keys()):

            if n - item >=0:
                n -= item
                st += R[item]

                P = []
                if "D" in R[item]:
                    for k in R:
                        if "D" in R[k]:
                            P.append(k)

                elif "L" in R[item]:
                    for k in R:
                        if "L" in R[k]:
                            P.append(k)

                elif "V" in R[item]:
                    for k in R:
                        if "V" in R[k]:
                            P.append(k)

                for p in P:
                    R.pop(p)

                break

    return st



def evaluate(st):
    R = {
        1:     "I",
        5:     "V",
        4:    "IV",
        10:    "X",
        9:    "IX",
        50:    "L",
        40:   "XL",
        100:   "C",
        90:   "XC",
        500:   "D",
        400:  "CD",
        1000:  "M",
        900:  "CM",
    }


    for item in reversed(R.keys()):
        if R[item] in st:
            st = st.replace(R[item], (str(item)+"/"))

    return sum(map(int, st.split("/")[:-1]))



with open("p89_roman.txt", "r") as f:
    rl = [line.strip("\n") for line in f.readlines()]

    print(sum([len(numeral)-len(minimal(evaluate(numeral))) for numeral in rl]))