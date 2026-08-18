# ---------------------------------------
# Program 129: Count Characters  
#Description:Counts all characters including letters, digits, and symbols.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH LENGTH NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i.isspace():
        COUNT=COUNT+0
    else:
        COUNT=COUNT+1
print('Characters Count-',COUNT)
