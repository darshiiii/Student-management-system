import csv
from csv import writer
import matplotlib.pyplot as plt
import pandas as pd

def add_stu():
    l=[]
    admission_no=int(input("Enter Admission Number : "))
    stu_name=input("Enter Student Name : ")
    classs=int(input("Enter Class : "))
    age=int(input("Enter Age : "))
    caste=input("Enter Caste : ")
    Father_name=input("Enter Father Name : ")
    mother_name=input("Enter Mother Name : ")
    phn_no=int(input("Enter mobile number : "))
    gender=input("Enter Gender : ")
    fees=int(input("Enter Fees : "))
    inst=int(input("Enter Number of installments of fees : (1,2,3)"))
    calc=fees/inst
    print(calc)

    l.append(admission_no)
    l.append(stu_name)
    l.append(classs)
    l.append(age)
    l.append(caste)
    l.append(Father_name)
    l.append(mother_name)
    l.append(phn_no)
    l.append(gender)
    l.append(fees)
    l.append(inst)
    l.append(calc)
    
    if(inst==1):
          m1=input("Enter Month 1 : ")
          l.append(m1)
    elif(inst==2):
          m1=input("Enter Month 1 : ")
          l.append(m1)
          m2=input("Enter Month 1 : ")
          l.append(m2)
    elif(inst==3):
          m1=input("Enter Month 1 : ")
          l.append(m1)
          m2=input("Enter Month 1 : ")
          l.append(m2)
          m3=input("Enter Month 1 : ")
          l.append(m3)
    print("Successfully Added To file....")
            
    with open('stu.csv', 'a') as f_obj:
            w = writer(f_obj)
            w.writerow(l)
            f_obj.close()


