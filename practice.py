'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
print()
print('----------task4--------')
year = int(input("Enter a year :"))
divisor = 400 #diving year by 400 will let us know if it is leap year and century year or not.
result = year % divisor #dividing given year by 400
if result == 0:
    print("The year is a century year and a leap year.")
else:
    print("It is not a leap year and a century year.")
