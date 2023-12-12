import csv
from csv import writer
import matplotlib.pyplot as plt
import pandas as pd
def del_stu():
        n1=int(input("Enter Admission Number : "))
        df = pd.read_csv('stu.csv', index_col='add_no')
        df = df.drop(n1)
        df.to_csv('stu.csv', index=True)
        print("Successfully Deleted From file....")

