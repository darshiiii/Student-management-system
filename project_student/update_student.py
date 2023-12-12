import pandas as pd
def update_stu():

   
    df = pd.read_csv("stu.csv")


    row_number = int(input("Enter row number : "))  
    column_name = input("Enter column Name : ")
    if(column_name=="stu_name" or column_name=="caste" or column_name=="father_name" or column_name=="mother_name" or column_name=="gender" or column_name=="1st_month" or column_name=="2nd_month" or column_name=="3rd_month"):
        value=input("Enter string you want to insert : ")
        df.loc[row_number, column_name] = value
        df.to_csv("stu.csv", index=False)
    elif(column_name=="class" or column_name=="age" or column_name=="phn_no" or column_name=="fees"):
        value=int(input("Enter value you want to insert : "))
        df.loc[row_number, column_name] = value
        df.to_csv("stu.csv", index=False)
    else:
        print("plzz enter correct column name...!!")

    print("CSV file updated successfully!")

    

    

'''
def update_stu():
        df=pd.read_csv("student.csv")
        new_val=input("Enter Name : ")
        df.loc[2,'StudentName']=new_val
        df.to_csv("student.csv",index=False)
'''