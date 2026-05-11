#a/b * (a-1)/(b-1) = 1/2

#a+b = n

#n > 10^12

# a(a-1)/b(b-1) = 1/2
#2a^2 - 2a = b^2 - b


#2a^2 - b^2 -2a + b = 0

#a = n-b

#2(n-b)^2 - b^2 -2(n-b) + b = 0

#2(n^2 + b^2 -2nb) - b^2 - 2n + 2b = 0

#b^2 + (2-4n)b + 2n^2 -2n = 0

#(2-4n)^2 -8n^2 + 8n >= 0

#(4 - 16n + 16n^2) -8n^2 + 8n >= 0

#8n^2 + -8n + 4 >= 0

#n^2 - n >= -1/2

#disc: (n - 1/2)^2 + 1/4 >= 0
#(n - 1/2)^2 + 1/4 = k^2

#k^2 - 1/4 = (n - 1/2)^2
#(4k^2 -1)/4 = (n - 1/2)^2

#1/2 * sqrt(4k^2-1) = n - 1/2

#n = 1/2 +- sqrt(4k^2-1)/2 = a + b

#4z^2 - 1 = y^2

#4z^2 - y^2 = 1

#x = 2z, x^2 - y^2 = 1
#(x+y)(x-y) = 1

#z = 1/2, y = 0

#---------------------------------------------------------------
#instead,

#let f(x) = x^2 - x
#because a/b * (a-1)/(b-1) = 1/2, so f(b) = 2f(a)

#then, 2f(15) = f(21), [15, 21] is a subset of T where T are triangular numbers

#Tx = (x(x-1))/2, sub a, b
#Ta = 1/2(Tb), 2(Ta-T(a-1)) (Tb-T(b-1))

def f(x):
    return x**2 - x

#because, a + b = n, and, n>10^12, therefore: 3f(x) > 10^12
#hence, x^2 - x -10^12/3 > 0
#x > ~575000, we can check in this range

found, y = True, 575000

while not found:
    D = 1 + 8*y*(y-1)

    if D & 15 not in {0,1,4,9}:
        y += 1
        continue

    k = D
    while k*k > D:
        k = (k + D // k) // 2

    if k*k == D:
        x = (1 + k) // 2
        print(x, y)
        found = True

    y += 1

# sadly this is incorrect, i solved for = 2 rather than = 1/2

a, b = 15, 21

while a + b <= 10**12:
    a, b = (
        3*a + 2*b - 2,
        4*a + 3*b - 3
    )

print(a)