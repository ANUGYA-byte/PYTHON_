# ---------------------------------------
# Program 22: Positive, Negative or Zero
# Description: Determines whether a given number is positive, negative, or zero.
# Author: Anugya Agrawal
# ---------------------------------------

number = float(input("ENTER NUMBER: "))

if number > 0:
    print(number, "NUMBER IS POSITIVE")
elif number < 0:
    print(number, "NUMBER IS NEGATIVE")
else:
    print(number, "NUMBER IS ZERO")

# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER: 12
# SAMPLE OUTPUT
# 12.0 NUMBER IS POSITIVE
#
# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER: -11
# SAMPLE OUTPUT
# -11.0 NUMBER IS NEGATIVE
#
# ---------------------------------------
# SAMPLE INPUT
# ENTER NUMBER: 0
# SAMPLE OUTPUT
# 0.0 NUMBER IS ZERO
# ---------------------------------------
