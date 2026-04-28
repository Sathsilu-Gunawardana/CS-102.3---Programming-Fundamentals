#Question 1

count = 1
total = 0

while count <= 5:
    marks = int(input("Enter your marks: "))
    count = count + 1
    total = total + marks

print ("\nYour total number of marks is:", total)

average = total / 5
                
print("\nYour average is:", average)

if average > 50:
    print("\nYou Passed!")

else:
    print("\nYou Failed!")


#Question 2

pin = int(input("Enter your pin: "))

while pin != 1234:
    print("Incorrect PIN, try again!")
    pin = int(input("Enter your pin: "))

print("Access granted")
    

#Question 3


count = 1
total = 0

while count <= 5:
    price = int(input("Enter the price of the grocery item: "))
    count = count + 1
    total = total + price

print("\nYour total grocery price is:", total)

if total > 5000:
    discounted = total * 80 / 100

    print("\nYou got 20% discount!")
    print("\nYour discounted price is:", discounted)

else:
    print("\nYou get no discount!")


#Question 4

count = 1
odd_count = 0
even_count = 0

while count <= 5:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        even_count = even_count + 1

    else:
        odd_count = odd_count + 1

    count = count + 1

print("\nTotal number of odd numbers is:", odd_count)
print("Total number of even numbers is:", even_count)


#Question 5

total = 0

deposit = int(input("Enter the deposite amount: "))

while deposit != 0:
    total = total + deposit
    deposit = int(input("Enter the deposite amount: "))

print("\nYour total deposited amount is:", total)

if total >= 10000:
    print("\nYou are a premium customer!")
else:
    print("\nYou are a regular customer!")

#Question 6

count = 1
password = input("Enter the password: ")

while count < 3 and password != 'admin':
    print("Incorrect Password!")
    count = count + 1
    password = input("\nEnter the password: ")

if password == 'admin':
    print("Login Successful!")
    
else:
    print("Account Locked!")

#Question 7

total = 0
count = 1

while count <= 3:
    units = int(input("Enter units used for month: "))
    total = total + units
    count = count + 1

print("\nTotal Units Consumed =", total)

if total > 300:
    print("\nHigh Usage!")
    
else:
    print("\nNormal Usage!")


#Question 8

count = 1
low_stock = 0

while count <= 5:
    stock = int(input("Enter the stock quantity: "))

    if stock < 10:
        low_stock = low_stock + 1

    count = count + 1

print("\nNumber of low stock products is:", low_stock)


#Question 9

count = 0
high_temp = 0

temperature = int(input("Enter the temperature: "))

while temperature != -1:
    
    if temperature > 30:
        high_temp = high_temp + 1
    
    temperature = int(input("Enter the temperature: "))

print("\nNumber of temperatures above 30 is:", high_temp)


#Question 10

count = 1

while count <= 5:
    sales = int(input("Enter the sales amount: "))

    if sales >= 5000:
        commission = sales * 10 / 100
        print("Commission is:", commission, "\n")

    else:
        print("No commission earned!\n")

    count = count + 1
