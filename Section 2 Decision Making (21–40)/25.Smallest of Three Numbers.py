# ---------------------------------------
# Program 25: Smallest of Three Numbers
# Description: Compares three numbers and finds the smallest value.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("ENTER NUMBER 1: "))
number2 = float(input("ENTER NUMBER 2: "))
number3 = float(input("ENTER NUMBER 3: "))

if number1 < number2 and number1 < number3:
    print(number1, "SMALLEST NUMBER")
elif number2 < number1 and number2 < number3:
    print(number2, "SMALLEST NUMBER")
elif number3 < number1 and number3 < number2:
    print(number3, "SMALLEST NUMBER")
else:
    print("ALL NUMBERS ARE EQUAL")

# ---------------------------------------
# SAMPLE INPUT-
# ENTER NUMBER 1: 1
# ENTER NUMBER 2: 2
# ENTER NUMBER 3: 3
#
# SAMPLE OUTPUT-
# 1.0 SMALLEST NUMBER
#
# ---------------------------------------
# SAMPLE INPUT-
# ENTER NUMBER 1: 1
# ENTER NUMBER 2: 1
# ENTER NUMBER 3: 1
#
# SAMPLE OUTPUT-
# ALL NUMBERS ARE EQUAL
# ---------------------------------------
