"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b

#Testing
assert divide(2, 0) == None #0 division
assert divide(10, 2) == 5 #whole number asnwer
assert divide(5, 2) == 2.5 #decimal asnwer
assert divide(0, 2) == 0 #answer is 0
"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

#Testing non-negative numebers
assert factorial(5) == 120
assert factorial(0) == 1


"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string
#Testing
assert reverse_string("hello") == "olleh" #simple 1 word
assert reverse_string("Abc") == "cbA" #upper & lower cases
assert reverse_string("-,./123") == "321/.,-" #symbols & numbers
assert reverse_string("a.  b") == "b  .a" #spaces
assert reverse_string("long sentences like this") == "siht ekil secnetnes gnol" # multiple words

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
#Testing
assert fibonacci(0) == 0 
assert fibonacci(5) == 5
try:
  assert fibonacci(-2) == -1 #leads to AssertionError. since negafibonacci isnt considered
except AssertionError: #error occurs, thus printing error message.
  print()
  print("----------------Exercise 4-------------")
  print("AssertionError occured because negafibonacci isn't considered in the code.")

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None
#Testing
# output True if email is correct(has '@' symbol, has domain, has TLD extension)
assert is_valid_email("ok@gmail.com") == True 
assert is_valid_email("hello@gmail.net") == True 
assert is_valid_email("hi@yahoo.org") == True
#invalid emails....
assert is_valid_email("wazihgmail.com") == False #(no '@' symbol)
assert is_valid_email('@com') == False #no domain between @ and com, no username
assert is_valid_email("hello@.com") == False#no domain
assert is_valid_email("hello@gmail") == False #no TLD extension
assert is_valid_email("@gmail.com") == False #no username
