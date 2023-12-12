
ch=0
while True:
    print("1. Add student")
    print("2. remove student")
    print("3. update student")
    print("4. exit")
    ch=int(input("Enter choice : "))
    if(ch==1):
        import add_student
        add_student.add_stu()
    elif(ch==2):
        import remove_student
        remove_student.del_stu()
    elif(ch==3):
        import update_student
        update_student.update_stu()
    elif(ch==4):
        print("Exiting.......")
        break
        
        