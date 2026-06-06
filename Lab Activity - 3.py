#Question 1

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print("\nBefore swapping a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swapping a = ", a, "b = ", b)


#Question 2

attendance = int(input("Enter attendance percentage without the % sign - "))

if attendance >= 75:
    print("\nYou are eligible for the exam")
    
else:
    print("\nYou are not eligible for the exams")


#Question 3
    
salary = int(input("Enter your salary: "))

if salary >= 100000:
    bonus = salary * 0.15

elif 50000 <= salary <= 99999:
    bonus = salary * 0.10

else:
    bonus = salary * 0.05

print("\nBonus =", bonus)


#Question 4

income = int(input("Enter your income: "))

if income >= 100000:
    tax = income * 0.20

elif 50000 <= income < 100000:
    tax = income * 0.10

else:
    tax = income * 0

print("\nYour tax amount is: ", tax)


#Question 5

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 == num2 == num3:
    print("\nAll numbers are equal")

elif num1 >= num2 and num1 >= num3:
    print("\nLargest number is: ", num1)

elif num2 >= num1 and num2 >= num3:
    print("\nLargest number is: ", num2)

else:
    print("\nLargest number is: ", num3)


#Question 6
    
gpa = float(input("Enter your GPA: "))
income = int(input("Enter your family's income: "))

if gpa >= 3.5 and income < 30000:
    print("\nYou get the full scholarship")

elif gpa >= 3.0 and income < 50000:
    print("\nYou get the partial scholarship")

else:
    print("\nYou get no scholarship")


#Question 7
    
weight = int(input("Enter your baggage's weight: "))

if weight <= 20:
    print("\nNo extra charge")

elif 21 <= weight <= 30:
    charge = (weight - 20) * 200
    print("\nExtra charge: ", charge)

else:
    print("\nBaggage not allowed")


#Question 8
    
pin = int(input("Enter your pin: "))
balance = int(input("Enter your account balance: "))
withdraw = int(input("Enter your withdrawal amount: "))

if pin == 1234:
    if withdraw > (balance - 500):
        print("\nInsufficient balance or minimum balance of 500 required")
        
    else:
        balance = balance - withdraw
        print("\nWithdrawal successful")
        print("Remaining balance:", balance)
        
else:
    print("\nIncorrect pin")
