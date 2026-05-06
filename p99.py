import sys
sys.set_int_max_str_digits(2122112212)

with open("p99_base_exp.txt", "r") as f:
    rl = f.readlines()

rl = [i.strip() for i in rl]
m = 0
L = 0

for l, pwr in enumerate(rl):
    n = eval("pow("+pwr+")")
    if n>m:
        m = n
        L = l

    #if l%10==0:
     #   print(l)

print(L+1)