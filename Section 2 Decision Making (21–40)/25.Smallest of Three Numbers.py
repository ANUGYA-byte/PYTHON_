# ---------------------------------------
# Program 25: Smallest of Three Numbers
# Description: Compares three numbers and finds the smallest value.
# Author: Anugya Agrawal
# ---------------------------------------


number1 = float(input("ENTER NUMBER 1: "))
number2 = float(input("ENTER NUMBER 2: "))
number3 = float(input("ENTER NUMBER 3: "))

smallest = min(number1, number2, number3)

print("SMALLEST NUMBER -", smallest)

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
