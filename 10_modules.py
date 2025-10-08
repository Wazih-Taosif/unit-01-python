"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print("--------------Task1------------")
import os
working_directory = os.getcwd() #stores the directory in the variable
print(f"The current folder (working directory) is {working_directory}")

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print("--------------Task2-----------")
print(os.listdir())#prints all the directories and files

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print("------------------Task3---------------")
if not os.path.exists("data"): #if the directory does not exit. it will create it
    os.mkdir("data")#creates the directory
else:
    print("Directory already exists.")

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print("-------------Task4-----------")
if os.path.exists("config.txt"): #checks if config.txt exists or not.
    print("File exists")
    print(os.path.abspath("config.txt"))#prints the path of the file
else:
    print("File not found")


"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print()
print("-------------Task5------------")
import sys

python_version = sys.version #stores the value of the python version
print(f"The python version being used is: {python_version}") #prints the python version I am using currently

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print()
print("------------------Task6----------")
platform = sys.platform #stores the value(platform)

#checks which output we get from sys.platform, and prints the user friendly names for the technical names.
if platform == "linux":
    print("The platform is Linux")
elif platform == "win32":
    print("The platform is Windows")
elif platform == "darwin":
    print("The platform is MacOS")
