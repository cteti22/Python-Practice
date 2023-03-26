
# https://www.learnpython.org/en/Hello%2C_World%21

# Basic printing in python

print("Hello World!")

x = 1

if x ==1:
    print("x is 1")

# Variables string,int,float: https://www.learnpython.org/en/Variables_and_Types
myInt = 7

print(myInt)

myFloat = 7.0
print(myFloat)

myFloat = float(7)
print(myFloat)


#Strings are defined either with a single quote or a double quotes.
myString = 'Hello'
print(myString)

myString = "Hello"
print(myString)

# concatinating integers
one = 1
two = 2
three = one + two
print(three)

# Concatinating strings
hello = "hello"
world = "world"
hw = hello + " "+ world
print(hw)



a,b = 3,4

print(a,b)

# This will not work!

# one = 1
# two = 2
# hello = "hello"

# print(one + two + hello)


myInt = 20
myFloat = float(10)
myString = "Hello"

if myInt == 20:
    print("Integer: %d" % myInt)
if isinstance(myFloat, float) and myFloat == 10.0:       #isinstance(object, type)
    print("Float is: %f" % myFloat)
if isinstance(myString, str) and myString == "Hello":
    print("String is: %s" % myString)


# Next Section: https://www.learnpython.org/en/Lists




