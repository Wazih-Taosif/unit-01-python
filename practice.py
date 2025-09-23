n1 = 0 # 1st term is 0
n2 = 1 # 2nd term is 1
nth_term = int(input("Enter the nth_term you want to see the fibonacci printed :")) # user says till which nth term we want to print the Fibonacci
nth = nth_term - 2 # this is done in order to print the first two terms (n1 and n2) 
while nth_term <= 0: #checking if nth term is valid or not.
    print("Enter a valid nth term please")
    nth_term = int(input("Enter the nth_term you want to see the fibonacci printed :"))
if nth_term == 1: #will just print 0
    print("Fibonacci sequence for {0} term is :".format(nth_term))
    print(n1)
if nth_term == 2: #Will print both 0 and 1
    print("Fibonacci sequence for {0} terms is :".format(nth_term))
    print(n1)
    print(n2)
if nth_term > 2:
    print("The Fibonacci is: ") #Prints the first 2 terms, 0 and 1
    print(n1)
    print(n2)
    while nth >= 1:
        n3 = n1 + n2 # the next term(n3) or the 'third' term is the sum of previous term(n1) and current term(n2)  
        n1 = n2 #current term(n2) becomes previous term(n1) for the next iteration
        n2 = n3 #next term(n3) becomes the current term(n2) for the next iteration
        print(n3) #printing all next term(n3) values, untill condition is False
        nth -= 1 