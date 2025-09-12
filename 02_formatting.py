"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
print()
print("-------task1------")
user_password = input("Enter password :") #user password
#used strip and lower to make sure the password is lowercase and has no extra space.
final_user_password = user_password.strip().lower()
user_login_password = input("Log in with the password :").lower()#user trying to log in using same password again.
if user_login_password == final_user_password:
    print("password is correct")
else:
    print("Password is wrong")
print()

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print("=====task2------")
#user input
input1 = input("Type something :").strip()
if input1 == "":#indicating nothing
    print("Invalid")
else:
    print("valid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print("-----task3------")
animal = input("Type the word cat :").lower().strip()#user inputs cat. 
animal_dog = animal.replace("cat", "dog")# replacign the word
print(animal_dog)
print()
"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print()
print("------task4-----")
name = input("Enter your name :").lower().strip()
age = input("Enter your age :").lower().strip()
print(name)
print(age)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
#user inputs
float1 = float(input("Enter a number :").strip())
float2 = float(input("Enter another number :").strip())
quotient = float1 / float2
result = f"The result is {quotient:.1f}"
print(result)