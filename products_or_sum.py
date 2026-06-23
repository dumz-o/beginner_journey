#"Write a Python script that takes two integers from user input. If the product of the numbers is greater than 1000, print their sum; otherwise, print their product."
#Let the user enter the desired numbers
n1 = input("Please enter value of first number: ")
n2 = input("Please enter value of second number: ")
# these are obviously the calculations for the number
x = int(n1) * int(n2)
y = float(n1) + float(n2)
# the condition for what to do based on the number calculated 
if x > 1000 :
    print( y )
else :
    print(x)
