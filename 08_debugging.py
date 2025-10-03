#First debugging project
print("First Task")
print()
text = "Hello, world, my name is" # given string
count = 0

for char in text:
    if char == " ": #only runs the following statement when it detects a space in the loop
       count += 1

print(count)

#Second debugging project
print("Second Task")
print()
print("give me a number")
n = int(input()) # takes a integer input

for num in range(1, n + 1): #n + 1 includes n too.
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

#Third debugging project
print("Third Task")
print()
num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.") # negative numbers cant be factorial as it is undefined.
else:
  result = 1
  for i in range(1, num + 1): # includes the inputted integer num. 
    result *= i   #result of the factorial of the given integer 'num'. 

  print(f"Factorial of {num} is {result}")


#Fourth debugging project
print("Fourth Task")
print()
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break