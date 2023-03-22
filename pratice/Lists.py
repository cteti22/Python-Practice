# https://www.learnpython.org/en/Lists

# Lists are very similar to arrays. 
# They can contain any type of variable, and they can contain as many variables as you wish. 
# Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.
# Python provides a method called .append() that you can use to add items to the end of a given list.

myList = []

myList.append(1)
myList.append(2)
myList.append(3)

print(myList[0])
print(myList[1])
print(myList[2])

for x in myList:
    print(x)


# Exercise

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

for x in 1,2,3:
    numbers.append(x)

strings.append("hello")
strings.append("world")

secondName = names[1]

print(numbers)
print(strings)
print(secondName)


# next section: https://www.learnpython.org/en/Basic_Operators
    



