#Question 1

total = 0
count_below_50 = 0

for i in range(6):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total += marks

    if marks < 50:
        count_below_50 += 1

average = total / 6

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Subjects below 50:", count_below_50)

if average >= 60 and count_below_50 == 0:
    print("\nExcellent Performance")
elif average >= 50:
    print("\nPass")
else:
    print("\nFail")


#Question 2

correct_pin = "1234"
balance = 10000

for attempt in range(3):
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        amount = int(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient balance")
        elif balance - amount < 500:
            print("Minimum balance of Rs. 500 must be maintained")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)
        break
    else:
        print("Incorrect PIN")

else:
    print("Account blocked (3 incorrect attempts)")


#Question 3

total = 0

for i in range(5):
    price = float(input(f"Enter price of item {i+1}: "))
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    total += price * quantity

# Apply discount
if total > 10000:
    discount = 0.25
elif total > 5000:
    discount = 0.15
else:
    discount = 0

discount_amount = total * discount
final_bill = total - discount_amount

print("\nTotal Bill:", total)
print("Discount:", discount_amount)
print("Final Amount:", final_bill)


#Question 4

balance = 0

while True:
    amount = int(input("Enter amount (0 to stop): "))

    if amount == 0:
        break

    balance = balance + amount

print("\nFinal Balance:", balance)

if balance < 0:
    print("Account Status: Overdrawn")
else:
    print("Account Status: Active")


#Question 5

total_units = 0

for i in range(4):
    units = int(input(f"Enter units for month {i+1}: "))
    total_units = total_units + units

if total_units <= 100:
    bill = total_units * 10

elif total_units <= 200:
    bill = (100 * 10) + (total_units - 100) * 15

else:
    bill = (100 * 10) + (100 * 15) + (total_units - 200) * 20

print("\nTotal Units:", total_units)
print("Total Bill:", bill)

if total_units > 400:
    print("Usage Category: High")
else:
    print("Usage Category: Normal")

#Question 6

low = 0
normal = 0
high = 0

for i in range(6):
    stock = int(input(f"Enter stock quantity for product {i+1}: "))

    if stock < 10:
        low += 1
    elif stock <= 50:
        normal += 1
    else:
        high += 1

print("\nLow stock items: ",low)
print("Normal stock items: ",normal)
print("High stock items: ",high)

#Question 7

high = 0
normal = 0
low = 0

while True:
    temp = int(input("Enter temperature (-1 to stop): "))

    if temp == -1:
        break

    if temp > 35:
        high = high + 1
    elif temp >= 20:
        normal = normal + 1
    else:
        low = low + 1

print("\nHigh temperatures:", high)
print("Normal temperatures:", normal)
print("Low temperatures:", low)

#Question 8

total_salary = 0
total_bonus = 0

for i in range(5):
    salary = float(input(f"Enter salary for employee {i+1}: "))

    if salary >= 100000:
        bonus = salary * 0.20
    elif salary >= 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    total_salary += salary
    total_bonus += bonus

    print(f"Employee {i+1} bonus: {bonus}\n")

print(f"\nTotal Salary Payout: {total_salary}")
print(f"Total Bonus Given: {total_bonus}")
