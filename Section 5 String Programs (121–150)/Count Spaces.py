# ---------------------------------------
# Program 128: Count Words
#Description:Counts the number of words separated by spaces in a string.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH LENGTH NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i.isspace():
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Spaces Count-',COUNT+1)
