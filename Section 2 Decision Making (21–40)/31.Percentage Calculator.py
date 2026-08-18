# ---------------------------------------
# Program 31: Percentage Calculator
# Description:Calculates the percentage obtained from the marks scored in different subjects
# Author: Anugya Agrawal
# ---------------------------------------

marks1 = float(input("ENTER MARKS IN SUBJECT 1: "))
marks2 = float(input("ENTER MARKS IN SUBJECT 2: "))
marks3 = float(input("ENTER MARKS IN SUBJECT 3: "))
marks4 = float(input("ENTER MARKS IN SUBJECT 4: "))
marks5 = float(input("ENTER MARKS IN SUBJECT 5: "))

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
#ENTER YOUR MARKS IN SUBJECT 1120
#ENTER YOUR MARKS IN SUBJECT 2130
#ENTER YOUR MARKS IN SUBJECT 3140
#ENTER YOUR MARKS IN SUBJECT 4140
#ENTER YOUR MARKS IN SUBJECT 5150
#ENTER YOUR TOTAL MAXIMUM MARKS  750
# ---------------------------------------
#SAMPLE IOUTPUT-
#PERCENTAGE CALCULATION 90.66666666666666

