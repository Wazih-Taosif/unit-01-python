#all inputs
computer = int(input("How many computers are available? "))
student = int(input("How many students are waiting? "))
typeofclass = str(input("What type of class is it? programming, research, or typing? "))
class_type = ['programming' , 'research' , 'typing']
accommodations = int(input("How many students need special acommodations? "))
time = int(input("How long is the class period? "))


# for programming
if typeofclass in class_type and typeofclass == "programming":
   if time >= 90:
       if computer >= 5:
           if computer > student:
               if accommodations > 1:
                   print("PASS: Has the right equipment")
           else:
               print("PASS: Should work with time correlation")
       else:
           print("FAIL: Not enough computers")
   else:
       print("FAIL: Class doesn't have enough time")
elif typeofclass in class_type and typeofclass == "research": #for reseach
   if time >= 45:
       if computer >= 5:
           if computer > student:
               if accommodations > 1:
                   print("PASS: Has the right equipment")
           else:
               print("PASS: Should work with time correlation")
       else:
           print("FAIL: Not enough computers")
   else:
       print("FAIL: Class doesn't have enough time")
elif typeofclass in class_type and typeofclass == "typing":
   if time >= 45:
       if computer >= 5:
           if computer > student:
               if accommodations > 1:
                   print("PASS: Has the right equipment")
           else:
               print("PASS: Should work with time correlation")
       else:
           print("FAIL: Not enough computers")
   else:
       print("FAIL: Class doesn't have enough time")
else:
    print("FAIL: Invalid class")