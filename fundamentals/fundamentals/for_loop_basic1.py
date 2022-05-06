# Basics
for count in range(151):
    print(count)


# Multiples of Five
for fives in range(1,201):
    print(fives*5)

# alternative
for fives in range(5,1001,5):
    print(fives)


# Counting, the Dojo Way
for dojo in range(1,101):
    if (dojo % 10 == 0):
        print("Coding Dojo")
    elif (dojo % 5 == 0 ):
        print("Coding")
    else:
        print(dojo)


# Whoa. That Sucker's Huge
huge = 0
for number in range(1,500001,2):
    huge += number
print(huge)
print('---------')


# Countdown by Fours
for fours in range(2018,0,-4):
    print(fours)
print('---------')


# Flexible Counter
lowNum = 1
highNum = 5
mult = 2
for number in range(lowNum,highNum,mult):
    print(number)