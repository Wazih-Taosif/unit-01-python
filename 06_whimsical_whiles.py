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

n1 = 0 # 1st term is 0
n2 = 1 # 2nd term is 1
nth_term = int(input("Enter the nth_term you want to see the fibonacci printed :")) # user says till which nth term we want to print the Fibonacci
nth = nth_term - 2 # this is done in order to print the first two terms (n1 and n2) 
while nth_term <= 0: #checking if nth term is valid or not.
    print("Enter a valid nth term please")
    nth_term = int(input("Enter the nth_term you want to see the fibonacci printed :"))
if nth_term == 1: #will just print 0
    print("Fibonacci sequence for {0} term is :".format(nth_term))
    print(n1)
if nth_term == 2: #Will print both 0 and 1
    print("Fibonacci sequence for {0} terms is :".format(nth_term))
    print(n1)
    print(n2)
if nth_term > 2:
    print("The Fibonacci is: ") #Prints the first 2 terms, 0 and 1
    print(n1)#1st term
    print(n2)#2nd term
    while nth >= 1:
        n3 = n1 + n2 # the next term(n3) or the 'third' term is the sum of previous term(n1) and current term(n2)  
        n1 = n2 #current term(n2) becomes previous term(n1) for the next iteration
        n2 = n3 #next term(n3) becomes the current term(n2) for the next iteration
        print(n3) #printing all next term(n3) values, untill condition is False
        nth -= 1 
    

