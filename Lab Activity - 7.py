# Question 1

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# a
print(fruits)
print()

# b
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print()

# c
count = 0

for item in fruits:
    count += 1
    
print("Length:", count)


# Question 2

colors = ["Red", "Blue", "Green"]

# a
colors.append("Yellow")
print(colors)
print()

# b
colors.insert(1, "Pink")
print(colors)
print()

# c
colors.remove("Blue")
print(colors)
print()

# d
removed = colors.pop()

print("Removed item:", removed)
print("Final List:", colors)


# Question 3

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90,100]

# a
print(numbers[:3])
print()

# b
print(numbers[-3:])
print()

# c
print(numbers[::2])
print()

# d
print(numbers[::-1])


# Question 4

students = ["Dulneth", "Bimsara", "Sadew", "Hirun", "Theshan"]

# a
for name in students:
    print(name)

print()

# b
for i, name in enumerate(students, start=1):
    print(i, ".", name)

print()

# c
count = 0

for name in students:
    if len(name) > 4:
        count += 1

print("Count:", count)


# Question 5

nums = [4, 7, 2, 7, 9, 1, 7, 5]

# a
count = nums.count(7)

print("7 appears", count, "times")
print()

# b
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print()

# c
nums.reverse()

print(nums)
print()

# d
copy_nums = nums.copy()
copy_nums.extend([10, 11, 12])

print("Original:", nums)
print("Copy:", copy_nums)


# Question 6

L1 = []
L2 = []

for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    L1.append(num)

print()

for i in range(4):
    text = input(f"Enter string {i+1}: ")
    L2.append(text)

L = []

for i in range(4):
    L.append(L1[i])
    L.append(L2[i])
    
print("\nL1 =", L1)
print("L2 =", L2)
print("\nL  =", L)


# Question 7

students = ["Sadew", "Hirun", "Dulneth", "Bimsara", "Theshan", "Nisal"]

name = input("Enter a name: ")

found = False

for student in students:
    if student.lower() == name.lower():
        found = True

if found:
    print("Student Present")
    
else:
    print("Student Not Found")


# Question 8

students = []

for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    age = int(input(f"Enter the age of student {i+1}: "))
    gpa = float(input(f"Enter the GPA of student {i+1}: "))

    students.append([name, age, gpa])
    print()
    
print("Student Details:")

for student in students:
    print(student)

highest = students[0]

for student in students:
    if student[2] > highest[2]:
        highest = student

print("\nHighest GPA Student:")
print(highest)

print("\nStudents with GPA >= 3.5:")

for student in students:
    if student[2] >= 3.5:
        print(student)


# Question 9

marks = []

for i in range(5):
    mark = int(input(f"Enter the marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

count = 0

for mark in marks:
    if mark < 50:
        count += 1

print("\nTotal marks =", total)
print("Average marks =", average)
print("Highest marks =", highest)
print("Lowest marks =", lowest)
print("Subjects below 50 =", count)

if average >= 75:
    print("\nGrade A")
    
elif average >= 60:
    print("\nGrade B")
    
elif average >= 50:
    print("\nGrade C")
    
else:
    print("\nGrade F")
