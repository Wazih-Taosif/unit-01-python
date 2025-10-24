"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print()
print("--------------Task1----------")
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("You cannot divide a number by 0. Please make sure the divisor is not 0.")
    except TypeError:
        print("Inputs must be numbers")
divide_numbers(10, 0)
divide_numbers(10, 4)

"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except FileNotFoundError:
        print("File does not exist.")
# Example usage:
read_file("nonexistent.txt")
        






