"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""
task_1_float = float(input("Type a number ")) #initial number
task_1_int = int(task_1_float)
#printing the result of the numbers.
print(task_1_float)
print(task_1_int)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
task_2_number = float(input("Task 2, Type a number ")) #number inputed by user
if task_2_number > 0:
    print("It's a positive number.")
elif task_2_number == 0:
    print("It's 0.")
else:
    print("It's a negative number.")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
task_3_number1 = int(input("Task 3, type a number ")) #first number
task_3_number2 = float(input("Task 3, type another number ")) #second number
task3_add = task_3_number1 + task_3_number2
task3_subtract = task_3_number1 - task_3_number2
task3_multiplication = task_3_number1 * task_3_number2
task3_division = task_3_number1 / task_3_number2 
#The result after adding, subtracting, mmultiplying, dividing.
print("Addition = " + str(task3_add) + " Subtraction = " + str(task3_subtract) + " Multiplication = " + str(task3_multiplication) + " Division = " + str(task3_division))

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#dictionary with variable fruits.
fruits = {
    "apples": 50,
    "bananas": 24,
    "mangoes": 12
}
print("The task 4 result, value of mangoes is:")
print(fruits["mangoes"])#getting value of mangoes.


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
task_5_string = "1,2,3,4,5,6,7"
task_5_tuple = 

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""

