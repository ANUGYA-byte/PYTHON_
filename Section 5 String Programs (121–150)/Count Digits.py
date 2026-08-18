STRING=input("ENTER THE STRING WHICH LENGTH NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i in '1234567890':
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Digits Count-',COUNT)
