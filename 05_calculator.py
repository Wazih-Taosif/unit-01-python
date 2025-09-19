print()
print()
print("Welcome to the Calculationator 9 Million!")
print()

# The 2 numbers that user will input...
x = float(input("Enter the first number :"))
y = float(input("Enter the second number :"))
print()
#line 11-20: all maths operation
message = """ Select Operation: 
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Exponential
7. Remainder
"""
print(message)

choice = input("Enter choice :")#users choice of operation


if choice == "1": # will do addition
    addition = x + y
    print(f"The Result : {addition}")
elif choice == "2": # subtraction
    subtraction = x - y
    print(f"The Result : {subtraction}")
elif choice == "3":# multiplication
    multiplication = x * y
    print(f"The Result : {multiplication}")
elif choice == "4": #division
    if y == 0: # Will not calculate if denominator(y) = 0.
        print("Cannot calculate the result, as denominator can't be 0.")
    else:
        division = x / y
        print(f"The Result : {division}") 
elif choice == "5": # floor division (rounding value down)
    if y == 0: # Will not calculate if denominator(y) = 0.
        print("Cannot calculate the result, as denominator can't be 0.") 
    else:
        floor_division = x // y
        print(f"The Result : {floor_division}")
elif choice == "6": #does exponential calculations
    exponential = x ** y
    print(f"The Result : {exponential}")
elif choice == "7": # gives the remainder after dividing first number by second number.
    if y == 0: # Will not calculate if denominator(y) = 0.
        print("Cannot calculate the result, as denominator can't be 0.")
    else:
        remainder = x % y
        print(f"The Result : {remainder}")
else:
    print("Invalid. No such option exist.") #user 'choice' is invalid.