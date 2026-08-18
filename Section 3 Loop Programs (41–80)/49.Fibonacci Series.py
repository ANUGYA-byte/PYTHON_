# ---------------------------------------
# Program 49: Fibonacci Series 
# Sequence where each term is the sum of the two preceding ones
# Author: Anugya Agrawal
# ---------------------------------------
NUMBER=int(input('ENTER NUMBER-'))
A,B=0,1
for i in range(1,NUMBER):
    print(A,end="")
    A,B=B,A+B
    
#ENTER NUMBER-5
#0112
