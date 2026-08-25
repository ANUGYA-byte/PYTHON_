# ---------------------------------------
# Program 31: Percentage Calculator
# Description:Calculates the percentage obtained from the marks scored in different subjects
# Author: Anugya Agrawal
# ---------------------------------------

marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("EEnter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))
marks4 = float(input("Enter marks in subject 4: "))
marks5 = float(input("Enter marks in subject 5: "))

marks = [marks1, marks2, marks3, marks4, marks5]

if any(mark < 0 or mark > 100 for mark in marks):
    print("INVALID MARKS")
else:
    total = sum(marks)
    percentage = total / 5

    print("TOTAL MARKS -", total)
    print("PERCENTAGE -", percentage, "%")

# ---------------------------------------
#SAMPLE INPUT-
#Enter marks in subject 1: 120
#Enter marks in subject 2: 130
#Enter marks in subject 3: 140
#Enter marks in subject 4: 150
#Enter marks in subject 5: 160
#ENTER YOUR TOTAL MAXIMUM MARKS  710
# ---------------------------------------
#SAMPLE IOUTPUT-
#PERCENTAGE CALCULATION 90.66666666666666

