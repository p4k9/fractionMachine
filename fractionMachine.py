# Write your code here :-)
from fractions import Fraction as frac
loop = "YES"
name = input("Hello, Welcome to the fraction machine. What's your name? ")
print("")

while loop == "YES" or loop == "Y":

    firstnum = input("Welcome " + name + ", What is your first fraction? (example: 1/2) ")
    print("")
    secondnum = input("and what is the second fraction? ")
    print("")
    function = input("What do you want to do? M, D, A, S ")
    function = function.upper()
    print("")

    if function == "M":
        answer = str(frac(firstnum) * frac(secondnum))
        print ("The answer is " + answer)
        print("")
        loop = input("Again? yes/no ")
        print("")
        loop = loop.upper()

    elif function == "D":
        answer = str(frac(firstnum) / frac(secondnum))
        print ("The answer is " + answer)
        print("")
        loop = input("Again? yes/no ")
        print("")
        loop = loop.upper()

    elif function == "A":
        answer = str(frac(firstnum) + frac(secondnum))
        print ("The answer is " + answer)
        print("")
        loop = input("Again? yes/no ")
        print("")
        loop = loop.upper()

    elif function == "S":
        answer = str(frac(firstnum) - frac(secondnum))
        print ("The answer is " + answer)
        print("")
        loop = input("Again? yes/no ")
        print("")
        loop = loop.upper()
    else:
        print("WOMP WOMP, that is an invalid math function. Lets try that again")
        print("")