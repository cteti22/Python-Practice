

# Ask the user for a number and check whether it is even or odd 
# and print out a meesage depending on if it is even or odd.

x=int(10)
y=int(5)
z=x/y
print(z)

num = int(input("Please input a number:"))

# check to see if the number is even or odd
print(num)

mod = num%2

if mod == 0:
    mult = num%4
    if mult == 0:        
     print("You chose an even number that is a multiple of four!")
    else:
       print("you chose an even number!")       
else:
    print("You chose an odd number!")


num = int(input("Enter a number to be divided:"))

check = int(input("Enter a number to divide by:"))

div = num%check

if div == 0:
   
   print(check,"divides evenly into", num,"!")

else:
   print(check,"does not divide evenly into"+ num,"!")