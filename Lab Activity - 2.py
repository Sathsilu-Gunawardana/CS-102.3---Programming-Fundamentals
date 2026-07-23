# Question 1

# Conditional statements in Python are used to execute certain blocks of code based on specific conditions.

# if - Runs code if the condition is True.
# elif - Checks another condition if the previous ones were False.
# else - Runs if all conditions above were False.

num1 = 10

if num1 > 0:
    print("\nPositive number")
    
elif num1 == 0:
    print("\nZero")
    
else:
    print("\nNegative number")

   
# Question 2
    
num1 = int(input("Enter a number: "))

if num1 > 0:
    print("\nPostive number")
    
else:
    print("\nNegative number")


# Question 3

num1 = int(input("Enter a number: "))

remainder = num1 % 2

if remainder == 0:
    print("\nThe number is even")
    
else:
    print("\nThe number is odd")


# Question 4

age = int(input("Enter your age: "))

if age >= 18:
    print("\nYou are eligible to vote")

else:
    print("\nYou are not eligible to vote")


# Question 5
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print()

if num1 > num2:
    print(num1, "is larger than", num2)
    
else:
    print(num2, "is larger than", num1)
    
    
# Question 6
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("\nThe largest number is: ", num1)
    
elif num2 > num1 and num2 > num3:
    print("\nThe largest number is: ", num2)
    
else:
    print("\nThe largest number is: ", num3)

    
# Question 7

num1 = int(input("Enter a number: "))

if num1 > 0:
    print("\nPositive number")
    
elif num1 == 0:
    print("\nZero")
    
else:
    print("\nNegative number")


# Question 8
    
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("\nYour grade is A")
    
elif marks >= 60:
    print("\nYour grade is B")
    
elif marks >= 50:
    print("\nYour grade is C")
    
else:
    print("\nYour grade is F")

    
# Question 9

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if username == "admin" and password == "1234":
    print("\nLogin successful")
    
else:
    print("\nLogin unsuccessful")


# Question 10

price = int(input("Enter purchasing price: "))

if price > 5000:
    discounted = price - (price * 20 / 100)
    print("\nDiscounted price = ", discounted)
    
elif price >= 2000:
    discounted = price - (price * 10 / 100)
    print("\nDiscounted price = ", discounted)
    
else:
    discounted = price
    print("\nYou get no discount")


# Bonus Question

units = int(input("Enter the number of units used: "))

if units <= 100:
    bill = units * 10

elif units <= 200:
    bill = (100 * 10) + (units - 100) * 15

else:
    bill = (100 * 10) + (100 * 15) + (units - 200) * 20

print("\nYour bill is: ", bill)
