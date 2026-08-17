# ---------------------------------------
# Program 23: Largest of Two Numbers
# Description: Compares two numbers and finds the larger one.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("ENTER NUMBER 1: "))
number2 = float(input("ENTER NUMBER 2: "))

if number1 > number2:
    print(number1, "LARGEST NUMBER")
elif number2 > number1:
    print(number2, "LARGEST NUMBER")
else:
    print("BOTH NUMBERS ARE EQUAL")

# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER 1: 2
# ENTER NUMBER 2: 2
#
# SAMPLE OUTPUT
# BOTH NUMBERS ARE EQUAL
#
# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER 1: 23
# ENTER NUMBER 2: 2
#
# SAMPLE OUTPUT
# 23.0 LARGEST NUMBER
#
# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER 1: 12
# ENTER NUMBER 2: 14
#
# SAMPLE OUTPUT
# 14.0 LARGEST NUMBER
# ---------------------------------------
