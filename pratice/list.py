# Take a list and print out numbers less than 5

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(list)
# Print 1 by 1
for ii in list:
    
    if ii < 5:
        print(ii)


# Append a new list and print it
newList = []

for x in list:
    
    if x < 5:
        newList.append(x)

print(newList)

# ask user for a number and print numbers less than that number from list.

varList = []
num = int(input("please enter a number:"))

for kk in list:

    if kk < num:
        varList.append(kk)

print(varList)


