"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

# Example usage:
try:
    divide_numbers(10, 0)
except ZeroDivisionError:
    print("You cannot divide a number by 0. Please make sure the divisor is not 0.")

"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()
try:
    read_file("nonexistent.txt")
except FileNotFoundError:
    import os
    os.mkdir("nonexistent.txt")



# Example usage:
read_file("nonexistent.txt")
