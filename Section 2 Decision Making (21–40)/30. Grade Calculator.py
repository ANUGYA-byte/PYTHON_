# ---------------------------------------
# Program 30: Grade Calculato
# Description:Calculates a student's grade based on their marks or percentage
# Author: Anugya Agrawal
# ---------------------------------------

PERCENTAGE=float(input("ENTER YOUR PERCENTAGE-  "))
if 90<=PERCENTAGE<=100:
    print("A GRADE")
elif 80<=PERCENTAGE<90:
    print("B GRADE")
elif 70<=PERCENTAGE<80:
    print("C GRADE")
elif 60<=PERCENTAGE<70:
    print("D GRADE")
else:
    print("E GRADE")

# ---------------------------------------
#SAMPLE -
#ENTER YOUR PERCENTAGE-  72
#C GRADE
# ---------------------------------------
#SAMPLE -
#ENTER YOUR PERCENTAGE-  33
#E GRADE
