# ---------------------------------------
# Program 48:  Factorial  
# Description: Product of all positive integers up to a given number.
# Author: Anugya Agrawal
# ---------------------------------------

F1=1
F2=1
NUMBER=int(input('ENTER NUMBER -'))
for i in range(1,NUMBER+1):
    F1=F1*i
print("FACTORIAL-",F1)

C=0
while C<(NUMBER):
    C=C+1
    F2=F2*C
print("FACTORIAL-",F2)

# ---------------------------------------
#SAMPLE 
"""ENTER NUMBER -5
FACTORIAL- 120
FACTORIAL- 120"""
