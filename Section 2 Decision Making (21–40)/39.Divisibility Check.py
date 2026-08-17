# ---------------------------------------
# Program 39: Divisibility Check
#  Checks whether one number is exactly divisible by another number.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------
NUMBER1=int(input('ENTER NUMBER WHOSE DIVISIBLITY NEED TO BE CHECK '))
NUMBER2=int(input('ENTER NUMBER BY WHICH DIVISIBLITY NEED TO CHECK'))
REMAINDER=NUMBER1%NUMBER2
if REMAINDER==0:
    print(NUMBER1,'IS EXACTLY DIVISIBLE BY ',NUMBER2)
else:
    print(NUMBER1,'IS NOT EXACTLY DIVISIBLE BY ',NUMBER2)


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

