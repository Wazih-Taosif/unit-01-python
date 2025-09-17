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
        print("Scalene Triangle")