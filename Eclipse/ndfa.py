import numpy as np
import pandas as pd
print(
    "========================================================================")
print("========================================================================")
print("================Formula Race Ticket Reservation System==================")
print("========================================================================")
print("========================================================================")

number = int(input("Enter number of vistors :"))
# creating an empty list for name , age , ticket class
name = []
age = []
classes = []
price = []
for i in range(0, number):
    n = input("Enter the Name of vistor "+str(i+1)+" : ")
    name.append(n)  # adding the element
    a = input("Enter the Age of vistor "+str(i+1)+" : ")
    age.append(a)  # adding the element
    c = input("Enter the classes of vistor "+str(i+1)+" : ")
    classes.append(c)  # adding the element
    if(c == 'A'):
        price.append(1500)
    elif(c == 'B'):
        price.append(1200)
    elif(c == 'C'):
        price.append(800)

    Sum = sum(price)
    space = ' '
print("========================================================================")
print("========================================================================")
print("===========================Vistor Report================================")
print("========================================================================")
print("========================================================================")
print("Name", "Age", "Classes","Price")


exam_data = {'Vistor Name': name,
             'Vistor Age': age,
             "Vistor class": classes,
             'Price': price}
labels = ['1', '2', '3', '4', '5', '6', '7',
          '8', '9', '20', '11', '12', '13', '14', '15']

df = pd.DataFrame(exam_data, index=labels)
print(df)
