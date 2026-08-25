# ---------------------------------------
# Program 39: Divisibility Check
#  Checks whether one number is exactly divisible by another number.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------
number1=int(input('ENTER NUMBER WHOSE DIVISIBLITY NEED TO BE CHECK '))
number2=int(input('ENTER NUMBER BY WHICH DIVISIBLITY NEED TO CHECK'))
REMAINDER=number1%number2
if NUMBER2 == 0:
    print("CANNOT DIVIDE BY ZERO")
elif number2 % number1 == 0:
    print("EXACTLY DIVISIBLE")
else:
    print("NOT EXACTLY DIVISIBLE")


# ---------------------------------------
#SAMPLE -
#ENTER NUMBER WHOSE DIVISIBLITY NEED TO BE CHECK 123
#ENTER NUMBER BY WHICH DIVISIBLITY NEED TO CHECK3
#123.0 IS EXACTLY DIVISIBLE BY  3.0
# ---------------------------------------
#SAMPLE -
#ENTER NUMBER WHOSE DIVISIBLITY NEED TO BE CHECK 124
#ENTER NUMBER BY WHICH DIVISIBLITY NEED TO CHECK3
#124.0 IS NOT EXACTLY DIVISIBLE BY  3.0

