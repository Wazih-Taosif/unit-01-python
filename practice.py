"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

number = input("Enter a number :")  #user inputs a number. Could be negative number too

list_number = list(number) #convert the user input from string to list
length_number = len(number) #calculating the length of the number. In other words the total number of digits the number has

if list_number[0] == "-": #This code will run if the user gives a negative number. It checks if the index 0 in the list has (-) sign or not
    del list_number[0] #removes the (-) sign from the list
    length_number = length_number - 1 # decreasing the length of the list because minus sign is removed

n = 0 #this indicates index value for list. n = 0 meaning it starts from index 0.
sum = 0 #At the start we have sum = 0

while length_number >= 1:
    sum = int(list_number[n]) + sum # New value of variable "sum" is adding previous indexes with current index
    n = n + 1 #Index number increments by 1
    length_number -= 1 #length number decrements by 1 so that it will end the loop when codition becomes false.
print(sum) # It prints the sum of the digits.

    