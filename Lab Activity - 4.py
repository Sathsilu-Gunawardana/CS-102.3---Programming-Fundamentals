# Question 1

# a
i = 0

while i <= 10:
    print(i)
    i = i + 1

# b
b = 10

while b >= 0:
    print(b)
    b = b - 1

    
# Question 2
    
total = 0
i = 1

while i <= 10:
    total = total + i
    i = i + 1

print("The sum is: ", total)


# Question 3

i = 1

while i <= 10:
    print("5 x", i, "=", 5 * i)
    i = i + 1


# Question 4
    
start = int(input("Enter a number to start the countdown: "))

while start >= 0:
    print(start)
    start = start - 1


# Question 5
    
total = 0
count = 1

while count <= 5:
    num = int(input(f"Enter your number {count}: "))
    total = total + num
    count = count + 1

print("\nThe total sum of your numbers is:", total)


# Question 6

total = 0
count = 1

while count <= 10:
    marks = int(input(f"Enter your marks for subject {count}: "))
    count = count + 1
    total = total + marks

print ("\nYour total number of marks for all subjects is:", total)

average = total / 10
                
print("Your average marks for a subject is:", average)

if average > 50:
    print("\nYou have Passed!")

else:
    print("\nYou have Failed!")


# Question 7

largest = 0
count = 1

while count <= 3:
    num = int(input(f"Enter your number {count}: "))

    if num > largest:
        largest = num

    count = count + 1

print("\nLargest number is", largest)


# Question 8

user_input = str("")

while user_input != "stop":
    print("\nHello")
    
    userinput = input("Type 'stop' to end, or anything else to see 'Hello' again: ")


# Question 9

num = int(input("Enter a number: "))

while num != -1:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    num = int(input("\nEnter a number: "))


# Question 10

number = int(input("Enter your number: "))

factorial = 1
count = 1

while count <= number:
    factorial = factorial * count
    count = count + 1
    
print("\nThe factorial of", number ,"is: ", factorial)
