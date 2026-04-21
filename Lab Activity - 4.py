#Question 1

#a

i = 0

while i < 11:
    print(i)
    i = i + 1

#b

b = 10

while b >= 0:
    print(b)
    b = b - 1

    
#Question 2
    
total = 0
a = 1

while a <= 10:
    total = total + a
    a = a + 1

print("The sum is: ", total)


#Question 3

m = 1

while m <= 10:
    print("5 x", m, "=", 5 * m)
    m = m + 1
xc

#Question 4
    
start = int(input("Enter a number to start the countdown: "))

while start >= 0:
    print(start)
    start = start - 1


#Question 5
    
total = 0
count = 1

while count <= 5:
    num = int(input("Enter a number: "))
    total = total + num
    count = count + 1

print("The total sum is:", total)


#Question 6

count = 1
total = 0

while count <= 10:
    marks = int(input("Enter your marks: "))
    count = count + 1
    total = total + marks

print ("\nYour total number of marks is:", total)

average = total / 10
                
print("\nYour average is:", average)

if average > 50:
    print("\nYou Passed!")

else:
    print("\nYou Failed!")


#Question 7
    
a = int(input("Enter your number: "))
count = 1

while count < 3:
    b = int(input("Enter your number: "))

    if b > a:
        a = b

    count = count + 1

print("Largest number is", a)


#Question 8

userinput = ""

while userinput != "stop":
    print("Hello")
    userinput = input("Type 'stop' to end, or anything else to see 'Hello' again: ")


#Question 9

answer = input("Enter a number: ")
number = int(answer)

while number != -1:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    answer = input("Enter a number: ")
    number = int(answer)


#Question 10

number = int(input("Enter your number: "))
factorial = 1
count = 1


while count <= number:
    factorial = factorial * count
    count = count + 1
    
print("The factorial of that number is: ", factorial)
