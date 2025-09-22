"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print()
print("------task1-------")
i_1 = 1 # starting value is 1
while i_1 <= 10: #till i_1 hits 10 it will print all numbers till 10
    print(i_1)
    i_1 += 1
print()

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print()
print("--------task2------")
i_2 = 10 #starting value is 10
while i_2 >= 1: #till i_1 hits 1 it will print all numbers till 1
    print(i_2)
    i_2 -= 1
print()
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print()
print("----------task3---------")
user_input_task3 = int(input("Enter a number to find the factorial :")) # user inputs the number
result_3 = 1 #default value of result is 1. Because we will do multiplication.
while user_input_task3 >= 1:
    result_3 = user_input_task3 * result_3 #changes value of result and stores the product of the variables user_input_task3 and result_3
    user_input_task3 -= 1 
print(result_3) # this is the result of the factorial


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print()
print()
print("--------task4------")
password = "password" #predefined password
guess = input("Guess the password :") # users guess
while guess != password:
    print("Try again") #user got the password wrong 
    guess = input("Guess the password :") # users guess

else:
    print("You guessed it right!") # if the user guesses the password right
print()

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
print()
print("-----------task6---------")

x = 0
y = 1
fibonacci = [x, y]
while x >= 0:
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)
    break
print(fibonacci)
 
 
 # user_input_6 = int(input("Which n terms of the fibonacci sequence you want to print :")) #The first n terms the user wants to print



