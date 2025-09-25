"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print()
print("-------task1--------")
for x in range(1, 11):
    print(x, end=" ") # going to print numbers from 1 to 10

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print()
print("---------task2")
for x in range(900, 1001, 10): #going to print numbers from 900 to 1000 by increment of 10
    print(x, end=" ")

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print()
print("---------task3----------")
for x in range(1, 101, 9): #prints numbers from 1 to 100 by increment of 9
    print(x, end=" ")

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print()
print("--------task4--------")
sum = 0
for x in range(1, 11):
    sum = x + sum #stores the sum of all numbers from 1 to 10
print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print("The output is * repeated several times in 5 rows.")