#Question 1

#What is a conditional statement in Python?

#Conditional statements in Python are used to execute certain blocks of code based on specific conditions.

#Explain if, elif and else

#if - Runs code if the condition is True.
#elif - Checks another condition if the previous ones were False.
#else - Runs if all conditions above were False.

#Python Program

num1 = 10

if num1 > 0:
    print("Positive number")
    
elif num1 == 0:
    print("Zero")
    
else:
    print("Negative number")

   
#Question 2
    
num1 = int(input("Enter a number: "))

if num1 > 0:
    print("Postive number")
    
else:
    print("Negative number")


#Question 3

num1 = int(input("Enter a number: "))

remainder = num1 % 2

if remainder == 0:
    print("The number is even")
    
else:
    print("The number is odd")


#Question 4

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")


#Question 5
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is larger than", num2)
    
else:
    print(num2, "is larger than", num1)
    
    
#Question 6
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print("The largest number is: ", num1)
    
elif num2 > num1 and num2 > num3:
    print("The largest number is: ", num2)
    
else:
    print("The largest number is: ", num3)

    
#Question 7

num1 = int(input("Enter a number: "))

if num1 > 0:
    print("Positive number")
    
elif num1 == 0:
    print("Zero")
    
else:
    print("Negative number")


#Question 8
    
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Your grade is A")
    
elif marks >= 60:
    print("Your grade is B")
    
elif marks >= 50:
    print("Your grade is C")
    
else:
    print("Your grade is F")

    
#Question 9

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if username == "admin" and password == "1234":
    print("Login successful")
    
else:
    print("Login unsuccessful")


#Question 10

price = int(input("Enter purchasing price: "))

if price > 5000:
    discounted = price - (price * 20 / 100)
    print("Discounted price = ", discounted)
    
elif price >= 2000:
    discounted = price - (price * 10 / 100)
    print("Discounted price = ", discounted)
    
else:
    discounted = price
    print("You get no discount")


#Bonus Question

units = int(input("Enter the number of units used: "))

if units <= 100:
    bill = units * 10

elif units <= 200:
    bill = (100 * 10) + (units - 100) * 15

else:
    bill = (100 * 10) + (100 * 15) + (units - 200) * 20

print("Your bill is: ", bill)
