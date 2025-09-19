'''
Exercise 1:
Check if an integer is greater than 10.
Return True if conditions are met, False otherwise.
'''
print()
print("---------Task1-------")

integer = 100
if integer > 10: # checking if integer if greater
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print()
print('-------task2-------')
age = 18
status = "student" 
if age < 18 or status == "student": #checking if the person is under 18 or is a student or not.
    print("Price is $10")
else:
    print("Price is $20")#print this if both are false


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print()
print('--------task3------')
task3_list = ["apples", "bananas", "guavas", "papayas", "mangoes"] #list with some fruits name
fav_fruit = input("What is your favourite fruit? ").strip().lower() #the user types their fav fruit
if fav_fruit in task3_list:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")
print()

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


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
print()
print('-------task5-----')
zone = input("Enter the zone :").strip().upper() 
weight = float(input("Enter the weight :")) 
cost = weight * 5 #cost for zone A
cost2 = weight * 7 #cost for zone B
if weight <= 0:
    print("Please type a correct weight. ")#error for inorrect weight
elif zone == "A" or zone == "ZONE A":
    print(f"Shipping cost is {cost} dollars per kilogram")
elif zone == "B" or zone == "ZONE B":
    print(f"Shipping cost is {cost2} dollars per kilogram")
else:
    print("Try again with correct zone please. ")#Output if wrong zone is inputed


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
print()
print('----------task6---------')
#user inputs
side1 = int(input("Enter value of one side of the triangle :"))
side2 = int(input("Enter value for second side :"))
side3 = int(input("Enter value for third side :"))
if side1 == side2 == side3: #for equilateral
    print("Equilateral Triangle")
elif side1 == side2 != side3 or side1 != side2 == side3:#isosceles
    print("Isosceles Triangle")
elif side1 != side2 != side3:
    if side1 + side2 < side3:
        print("Invalid Triangle.")
    elif side1 + side3 < side2:
        print("Invalid Triangle.")
    elif side2 + side3 < side1:
        print("Invalid Triangle")
    else:
        print("Scalene Triangle")#scalene
