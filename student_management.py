student={}
while True:
    print("\n-----WELCOME TO OUR MANAGEMENT SYSTEM-----\n")
    print("1.Add student.\n")
    print("2.View student.\n")
    print("3.Check result.\n")
    print("Exit.\n")

    ch=int(input("Enter your choice from the above options\n"))

    if ch==1:
        name=input("enter student name:")
        marks=int(input("enter student marks:"))

        student[name]=marks

        print("Student record added successfully\n")

    elif ch==2:
        

        if  not student:
            print("There is no student found")

        else:
            for name,marks in student.items():
                print("student found :")
                print(name,":",marks)

                                   
                                   

    elif ch==3:
        name=input("enter your name:")

        if name in student:
            print("student found\n")
            marks=student[name]
            if marks<=40:
                print("FAIL")
            else:
                print("PASS")
        else:
            print("no student found")

    elif ch==4:
        print("Exiting.....")
        break
    else:
        print("invalid input")
        

