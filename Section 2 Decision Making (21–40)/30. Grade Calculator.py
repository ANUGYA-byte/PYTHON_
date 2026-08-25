# ---------------------------------------
# Program 30: Grade Calculato
# Description:Calculates a student's grade based on their marks or percentage
# Author: Anugya Agrawal
# ---------------------------------------

PERCENTAGE=float(input("Enter your  percentage-  "))
if 90<=PERCENTAGE<=100:
    print("A GRADE")
elif 80<=PERCENTAGE<90:
    print("B GRADE")
elif 70<=PERCENTAGE<80:
    print("C GRADE")
elif 60<=PERCENTAGE<70:
    print("D GRADE")
elif PERCENTAGE < 0 or PERCENTAGE > 100:
    print("Invalid percentage")
else:
    print("E GRADE")

# ---------------------------------------
#SAMPLE -
#Enter your  percentage-  72
#C GRADE
# ---------------------------------------
#SAMPLE -
#Enter your  percentage-  33
#E GRADE
