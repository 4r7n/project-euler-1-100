sundays = 0

year = 1900  #we are going to simulate each day up to 30 dec 2001 and keep track of sundays
month = 0
date = 0
day = 0

def increment():
    global day, date, month, year, sundays

    day += 1
    day %= 7  #day is week day, as opposed to the date, which for instance would be *20* Dec 1925

    date+=1

    if month in [0, 2, 4, 6, 7, 9]:  #31 day months
        if date==31:
            date = 0
            month+=1

    elif month==11:
        if date==31:  #december end, which increments the year
            date = 0
            month = 0
            year+=1

    elif month in [3, 5, 8, 10]:
        if date==30:
            date = 0
            month+=1

    else:
        if (year % 4 == 0 and year%100 != 0) or (year%400 == 0): #febuaray leap year logic, if its either every 400 centuries or on a 4th year not on a century
            if date == 29:
                date = 0
                month += 1
        else:
            if date == 28:
                date = 0
                month += 1

    if day==6 and date==0:  #as we change date to 0 via functions, we add sundays here
        sundays+=1


while not(date==0 and month==0 and year==1901):
    increment()

sundays = 0  #i didnt check what day 1jan 1901 is, so we get here first, then reset the sundays ;)

while not(date==30 and month==11 and year==2000):
    increment()

print(sundays)