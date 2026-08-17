# ---------------------------------------
# Program 24: Largest of Three Numbers
# Description: Compares three numbers and finds the largest value.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("ENTER NUMBER 1: "))
number2 = float(input("ENTER NUMBER 2: "))
number3 = float(input("ENTER NUMBER 3: "))

if number1 > number2 and number1 > number3:
    print(number1, "LARGEST NUMBER")
elif number2 > number1 and number2 > number3:
    print(number2, "LARGEST NUMBER")
elif number3 > number1 and number3 > number2:
    print(number3, "LARGEST NUMBER")
else:
    print("ALL NUMBERS ARE EQUAL")

# ---------------------------------------
# SAMPLE INPUT-
# ENTER NUMBER 1: 1
# ENTER NUMBER 2: 2
# ENTER NUMBER 3: 3
#
# SAMPLE OUTPUT-
# 3.0 LARGEST NUMBER
#
# ---------------------------------------
# SAMPLE INPUT-
# ENTER NUMBER 1: 5
# ENTER NUMBER 2: 5
# ENTER NUMBER 3: 5
#
# SAMPLE OUTPUT-
# ALL NUMBERS ARE EQUAL
# ---------------------------------------
