#Question 1

print("Sathsilu Gunawardana")
print("Ananda College")


#Single Line Comment

"""
Multiline Comment
This is the second line
"""

#To help other programmers understand the code by providing context, explanations, and documentation


#Question 2

result = 22/7
print("the value of 22/7 is", result)


#Question 3

"""
What is meant by concatenation?
Concatenation means joining two or more strings together to form a single string. 
"""

operation = "sum"
total = 8

print(operation + " is " + str(total))


#Question 4

length = 10
width = 5

area = length * width

print("The area of a rectangle with length " + str(length) + " and with " + str(width) + " is " + str(area))


#Question 5

name = input("Enter your name: ")

print("\nHello " + name + ", welcome to NSBM!")
print(type(name))


#Question 6

birth_year = input("Enter your birth year: ")

birth_year = int(birth_year)

print("\nYour birth year is:", birth_year)
print(type(birth_year))

#Typecasting is the process of converting a value from one data type to another.


#Question 7

birth_year = int(input("Enter your birth year: "))

age = 2025 - birth_year

print("\nYour age is:", age)


#Bonus Question

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nAddition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Power:", num1 ** num2)
