from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print()
print("---------------Task1------------")
datetime_now = datetime.now() #stores the current date and time.
print(datetime_now)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print()
print("--------------------Task2------------")
current_date = datetime_now.strftime("%m/%d/%Y/ %H:%M:%S") #stores the value of current date and time, which is also formated
print(current_date)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print()
print("-----------------Task3--------------")
string1 = "01/30/2025"
string2 = "01/10/2025"
#converting the string to date
date1 = datetime.strptime(string1, "%m/%d/%Y")
date2 = datetime.strptime(string2, "%m/%d/%Y")
print(date1)
print(date2)
diff_day = abs(date2 - date1) # calculating the difference of days between the dates
print(f"Difference in days is: {diff_day}")

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
print("------------Task4----------")
#user inputs their birth day, month, year
day = input("Enter your birth day: ")
month = input("Enter your birth month as a zero-padded number: ")
year = input("Enter your four digit birth year: ")

birthdate_string = f"{month}/{day}/{year}" #writing the user input in one string
birthdate = datetime.strptime(birthdate_string, "%m/%d/%Y")#converts the string to date

current_date2 = datetime.now()#gets current date and time

user_age_days = abs(current_date2 - birthdate) #gives exact days difference

days_difference = user_age_days.days

user_age = days_difference / 365 #converting days difference to years difference

print(f"Your current age is {user_age:.2f} years")