print()
print()
#all inputs
computers = int(input("Number of computers :"))
students = int(input("Number of students :"))
class_type = input("Type of class :").strip().lower()
accommodations = int(input("Number of accommodations :"))
class_period = int(input("How long is the period? :"))

list_of_classes = ["programming", "research", "typing"] #only these classes are available.

#Line 13-17: Maths
remaining_students = students - accommodations      #students left after accommodations students got priority
remaining_computers = computers - accommodations     # computers remaining after students with accommodations got priority
waiting_students = remaining_students - remaining_computers  # students who did not get a computer, and thus is waiting.
groups_of_waiting_students = (waiting_students + computers - 1) // computers # This formula calculates how many groups of students are waiting for their turn. 
waiting_time = groups_of_waiting_students * 45 #Total time that the students who did not get a computer might have to wait for their turn.

#if class_type is not present in the list, it won't run any further codes.
if class_type not in list_of_classes:
    print("wrong class type")
else:
    #line 24-26: checks if computers less than 5 and if class is programming, if True then students cant do the class.
    if computers < 5:
        if class_type == "programming":
            print("Not enough computers for programming")


    #line 30-40: since computer >= students, everyone will get computers. But class duration might be adequate or not.
    if computers >= students:
        if class_type == "programming":
            if class_period >= 90: #checking if class time is adequate or not
                print("There are enough computers for everyone.")
            else:
                print("There are enough computers for everyone, but class duration will be less than 90 minutes.")
        elif class_type == "research" or class_type == "typing":
            if class_period >= 45: #checking if class time is adequate or not
                print("There are enough computers for everyone.")
            else:
                print("There are enough computers for everyone, but class duration will be less than 45 minutes.")

    # lines 43-53: There will be few students who will wait. Thus these codes tells how long they might need to wait for their turn.
    elif computers < students:
        if class_type == "programming" and computers >= 5:
            if class_period > (90 + waiting_time): #if class period is greator than 90(normal class time) + the waiting time, then all students will get computers
                print("All students will get computers within the class duration.")
            else:
                print(f"Class will proceed, but {waiting_students} students needs to wait about {waiting_time} minutes")   
        elif class_type == "research" or class_type == "typing":
            if class_period > (45 + waiting_time): #if class period is greator than 45(normal class time) + waiting time for students who did not get computers, then all students will get computers
                print("All students will get computers within this class duration.")
            else:
                print(f"Class will proceed, but {waiting_students} students needs to wait about {waiting_time} minutes")

#beneath is the Task for which I have the above code
"""
5. Computer Lab Monitor

Your Job: 
You are the technology resource manager! Computer labs are precious resources that need careful coordination.  
Programming classes need more time and specialized setups, while research projects have different requirements. 
Students with accommodations need priority access, but you also can't leave other students waiting indefinitely. 
Your system needs to juggle time requirements, accessibility needs, and resource availability to keep the digital 
learning flowing smoothly.

Your Code Must Ask For:
How many computers are available?
How many students are waiting?
What type of class? (programming, research, typing)
How many students need special accommodations?
How long is the class period? (in minutes)

Rules You Must Code:
Programming classes need at least 90 minutes, others need 45 minutes
Students with accommodations get computers first
If not enough computers, calculate wait time (assume 45 min per group)
Must have at least 5 computers available to run programming class
"""