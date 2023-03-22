# get a number from the user and print out all numbers that are divisors of that number
num = int(input("Please enter a number: "))
div = range(1,num+1)
newList = []

for x in div:

    if num%x == 0:

        newList.append(x)
        

print(newList)





          