# ---------------------------------------
# Program 37: Calculator Using if-else
# Performs basic arithmetic operations using if-else statements.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------

print("---------------------------------------# ---------------------------------------")
print("                                            MENU                                                 ")
print("---------------------------------------# ---------------------------------------")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.REMAINDER")
print("6.EXPONENT")


CHOICE=int(input('ENTER YOUR CHOICE-'))
if CHOICE==1:
    NUMBER1=float(input('ENTER NUMBER 1-'))
    NUMBER2=float(input('ENTER NUMBER 2-'))
    RESULT=NUMBER1+NUMBER2
    print ('ANSWER-',RESULT)
    
elif CHOICE==2:
    NUMBER1=float(input('ENTER NUMBER 1-'))
    NUMBER2=float(input('ENTER NUMBER 2-'))
    RESULT=NUMBER1-NUMBER2
    print ('ANSWER-',RESULT)

elif CHOICE==3:
    NUMBER1=float(input('ENTER NUMBER 1-'))
    NUMBER2=float(input('ENTER NUMBER 2-'))
    RESULT=NUMBER1*NUMBER2
    print ('ANSWER-',RESULT)

elif CHOICE==4:
    NUMBER1=float(input('ENTER DIVIDEND -'))
    NUMBER2=float(input('ENTER DIVISOR-'))
    RESULT=NUMBER1/NUMBER2
    print ('ANSWER-',RESULT)
    
elif CHOICE==5:
    NUMBER1=float(input('ENTER DIVIDEND -'))
    NUMBER2=float(input('ENTER DIVISOR-'))
    RESULT=NUMBER1%NUMBER2
    print ('ANSWER-',RESULT)    

elif CHOICE==6:
    NUMBER1=float(input('ENTER NUMBER -'))
    NUMBER2=float(input('ENTER NUMBER OF T-'))
    RESULT=NUMBER1**NUMBER2
    print ('ANSWER-',RESULT)

# ---------------------------------------
#SAMPLE -
#---------------------------------------# ---------------------------------------
#                                            MENU                                                 
#---------------------------------------# ---------------------------------------
#1.ADDITION
#2.SUBTRACTION
#3.MULTIPLICATION
#4.DIVISION
#5.REMAINDER
#6.EXPONENT
#ENTER YOUR CHOICE-1
#ENTER NUMBER 1-3
#ENTER NUMBER 2-2
#ANSWER- 5.0

#ENTER YOUR CHOICE-3
#ENTER NUMBER 1-3
#ENTER NUMBER 2-4
#ANSWER- 12.0
