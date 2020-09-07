### problem 1: Write a python program to accept two integers and check whether they are equal or not.
def isEqual(args):
    a, b = args
    if a == b:
        print("{0} is equal to {1}".format(a, b))
    else:
        print("{0} is not equal to {1}".format(a, b))

inputInt = [' ' for i in range(2)]
i = 0
while i < 2:
    inputInt[i] = int(input("Please input the integer no {}: ".format(i+1)))
    i+=1
isEqual(inputInt)
### problem 2: Write a python program to check whether a given number is positive or negative.
def isSign(a):
    if a > 0:
        print("{0} is a positive number".format(a))
    elif a < 0:
        print("{0} is a negative number".format(a))
    else:
        print("{0} is zero, neither positive or negative".format(a))


while True:
    inputInt = input("Please input the integer: ")
    if inputInt == "stop":
        print("You requested to stop. Good bye!")
        break
    else:
        isSign(int(inputInt))
### problem 3: Write a python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.
def whichCordinate(x, y):
    if x > 0 and y > 0:
        print("({0},{1}) is in 1st quadrant".format(x,y))
    elif x < 0 and y < 0:
        print("({0},{1}) is in 3rd quadrant".format(x,y))
    elif x < 0 and y > 0:
        print("({0},{1}) is in 2nd quadrant".format(x,y))
    elif x > 0 and y < 0:
        print("({0},{1}) is in 4th quadrant".format(x,y))
    else:
        print("({0},{1}) is the origin".format(x,y))


while True:
    x = input("Please input x cordinate: ")
    y = input("Please input y cordinate: ")
    if x == "stop" or y == "stop":
        print("You requested to stop. Good bye!")
        break
    else:
        whichCordinate(int(x),int(y))
### problem 4: Write a python program to check whether an alphabet is a vowel or consonant.
def isVowel_Consonant(x):
    vowel = "aeiou"
    consonant = "bcdfghjklmnpqrstvwxz"
    x = x.lower()
    if x in vowel:
        print("{0} is a vowel".format(x))
    elif x == "y":
        print("{0} is sometimes vowel not consonant".format(x))
    elif x in consonant:
        print("{0} is a consonant".format(x))
    else:
        print("its not an alphabet")


while True:
    x = input("Please input alphabet: ")
    if x == "stop":
        print("You requested to stop. Good bye!")
        break
    else:
        for i in x:
            isVowel_Consonant(i)
### problem 5: Write a python program to check whether a number is a even or odd.
def isEven_odd(a):
    if a % 2 != 0:
        print("{0} is an odd number".format(a))
    elif a == 0:
        print("{0} is neither an even nor an odd number".format(a))
    else:
        print("{0} is an even number".format(a))


while True:
    inputInt = input("Please input the integer: ")
    if inputInt == "stop":
        print("You requested to stop. Good bye!")
        break
    else:
        isEven_odd(int(inputInt))