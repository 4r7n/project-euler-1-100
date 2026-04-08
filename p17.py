#lets define some numbers in english

#luckily, we dont need to manually do all 1000 (should i say one thousand), only a few, but i guess one could if wanted

base1 = {
1: "one",
2: "two",
3: "three",
4: "four",
5: "five", #i shouldve made the keys strings, but realised that too late
6: "six",
7: "seven",
8: "eight",
9: "nine",
}

tens = {
1: "eleven",
2: "twelve",
3: "thirteen",
4: "fourteen",
5: "fifteen",
6: "sixteen",  #this is a special case as these dont follow the conventional rules of the rest
7: "seventeen", #i guess the last 4 do but whatever, its not worth the stress
8: "eighteen",
9: "nineteen",
}

base2 = {
1: "ten",
2: "twenty",
3: "thirty",
4: "forty",
5: "fifty",
6: "sixty",
7: "seventy", #the last 4 have a conistent theme, maybe its worth the stress but too late now!
8: "eighty",  #however im guessing it has something to do with how language evolves
9: "ninety",
}

#now we can start defining numbers!

def letters(n):
    n = str(n)

    if len(n)==4:
        num = "onethousand" #because we wont need to check any 4digit numbers greater than 1000

    elif len(n)==1:
        num = base1[int(n)] #second easiest, just the dict, we wont need zero too

    elif len(n)==2:
        if n[1] == "0":
            num = base2[int(n[0])] #if number is of form x0, we can use the dict

        elif n[0]=="1": #same with 1x
            num = tens[int(n[1])]

        else:
            num = base2[int(n[0])]+base1[int(n[1])] #base 2 + base 1, simple


    else: #now for the hardest part (not so hard however)
        if n[1:]=="00":
            num = base1[int(n[0])]+"hundred"

        elif n[1]=="0":  #im guessing you could make this recursively or something, but logic from now on follows the same as before, but with "hundred and" added
            num = base1[int(n[0])]+"hundredand"+base1[int(n[2])]

        elif n[2]=="0":
             num = base1[int(n[0])]+"hundredand"+base2[int(n[1])]

        elif n[1]=="1":
             num = base1[int(n[0])]+"hundredand"+tens[int(n[2])]

        else:
            num = base1[int(n[0])]+"hundredand"+base2[int(n[1])]+base1[int(n[2])]

    return num


print(sum([len(letters(i)) for i in range(1, 1001)]))  #now we sum up all the lengths of the words