"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print()
print("-----------------Task1---------------------")
def greeting(name):
    """
    Greets hello to "name"

    "Hello, {name}"
    """
    print(f"Hello, {name}")
greeting("Wazih")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print()
print("--------------Task2--------------")
def squared_number(num1):
    """
    Returns the squared value of an integer
    
    formula: num1 ** 2
    """
    return num1 ** 2
squared_result = squared_number(3) #returns and stores the squared value
print(squared_result)
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
print()
print("----------------------Task3--------------------")
def even_odd(num2):
    """
    Returns True if the number is even, False if the number is odd

    using the formula num2 % 2 == 0, to find if it is even. otherwise it is odd.
    """
    if num2 % 2 == 0:
        return True
    else:
        return False
even_odd_result = even_odd(5)#finding if the argument number is even or odd
print(even_odd_result)


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print()
print("------------------Task4---------------")
def rectangle_area(length, width):
    """
    returns the area of the rectangle

    formula: length * width
    """
    return length * width #area of the rectangle
rectangle_area_result = rectangle_area(10 ,5)#finding area of rectangle
print(rectangle_area_result)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
print("---------------Task5------------")
def celsius_fahrenheit(temp_in_c):
    """
    converting a temperature from celsius to fahrenheit

    formula: ((9/5) * Temp_in_c) + 32
    """
    return ((9 / 5) * temp_in_c) + 32
temp_in_f = celsius_fahrenheit(10)
print(temp_in_f)


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print()
print("----------------Task6------------")
def avg(list1):
    """
    takes a list of numbers, and returns the average(mean)

    formula: sum(list1) / len(list1)
    """
    return sum(list1) / len(list1)
avg_result = avg([2, 2])#avg of the numbers in the list.
print(avg_result)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print()
print("-----------------Task7--------------")
def price_quantity(price, quantity, discount = 0.0):
    """
    gives the total payment of a commodity. calculates total depending on quantity, and discount if avaiable.

    formula: (price * quantity) - ((price * discount) * quantity)
    """
    return (price * quantity) - ((price * discount) * quantity)
total_payment = price_quantity(100, 2, 0.10) #stores the total 
print(total_payment)