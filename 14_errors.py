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
        print("Result:", result) #prints the quotient of the two number
    except ZeroDivisionError:
        print("You cannot divide a number by 0. Please make sure the divisor is not 0.")#if num2 is 0, it will print this error msg.
    except TypeError:
        print("Inputs must be numbers")#error msg: if input is a letter

#examples
divide_numbers(10, 0)
divide_numbers(10, "a")
divide_numbers(10, 2)#valid example

"""
Example 2: Opening Files
"""
print()
print("--------------Task2------------")
def read_file(filename):
    try:
        #opens file, reads and save contents, then prints content
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except FileNotFoundError:
        print("File does not exist.")#error msg: if file does not exist.
# Example usage:
read_file("nonexistent.txt")
        
"""
Example 3: List Items
"""
print()
print("-----------Task3----------")
def get_item(lst, index):
    try:
        #gives item of specific index in a list
        item = lst[index]
        print("Item:", item)
    except IndexError: #wrong index inputed. or not enough item with equivalent index in the list.
        print("Wrong index. Please make sure the list has correct amount of index.")
# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
get_item(my_list, 2)


"""
Example 4: Dictionaries
"""
print()
print("----------Task4---------")

def get_value(dictionary, key):
    try:
        #gives value for respective key in a dictionary
        value = dictionary[key]
        print("Value:", value)
    except KeyError: #non existent key inputed.
        print("No such key exists in the dictionary.")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
get_value(my_dict, "a")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
print()
print("----------------Task5-------------")
def process_file(filename):
    try:
        #opens file, and reads content
        with open(filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError: #non existent file
        print("Error: File not found.")
    else: #file exists, thus content is printed
        print("File contents:", contents)
    finally:
        print()
        print("---------Process completed---------")

# Example usage:
process_file("nonexistent.txt")#leads to error
process_file("example.txt") #doesn't lead to error


