import math #to allow to use the square root and ceil functions, it will be importnant later



def factor(n, x): #(is x a factor of n?)
    return ((n/x)==int(n/x)) #true if n/x is an integer, else false



def isPrime(n): #to validate if numbers are prime
    if n<1:
        return

    if n in [1, 2]:
        return bool(-1+n) #base cases, because i am lazy

    for i in range(2, math.ceil(math.sqrt(n))+1): #iterate through the numbers from 2 to the ceiling of the square root of n (you may be able to use floor as opposed to ceiling, but im unsure)
        #this is as a factor of n to check wont be divisible by a number greater than the square root of n, as we wouldve went past it

        if factor(n, i): #via the function we just made
            return False  #if there is an integer factor, we can deduce it to be not prime

    return True #if none of the divisions lead to an int, it's a prime!


largeInteger = 600851475143

for i in range(math.ceil(math.sqrt(largeInteger)), 1, -1): #we descend from 600851475143, but thankfully, we only need to check from the square root of the number
    #as stated earlier, we dont need to check greater factors for prime numbers than their square root, and that logic applies here

    if factor(largeInteger, i) and isPrime(i): #as we are descending, the first prime factor will be the greatest
        print(i)
        break #stop the loop


