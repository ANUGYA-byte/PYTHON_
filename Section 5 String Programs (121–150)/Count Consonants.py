# ---------------------------------------
# Program 126: Count Digits  
# Description: Counts how many numeric digits are present in a string.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH LENGTH NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i.isdigit() :
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Digits Count-',COUNT)
