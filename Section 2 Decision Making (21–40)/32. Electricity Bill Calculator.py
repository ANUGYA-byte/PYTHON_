# ---------------------------------------
# Program 32 Eectricity Bill Calculator.
### Description: Calculates the electricity bill based on the units of electricity consumed.
#| Units consumed |    Rate |
#| -------------- | ------: |
#| 0–100           | ₹2/unit |
#| 101–200        | ₹3/unit |
#| 201–300        | ₹5/unit |
#| Above 300    | ₹7/unit |

# Author: Anugya Agrawal
# ---------------------------------------

UNITS=float(input('ENTER UNITS-'))
if UNITS<=100:
     print ('AMOUNT-',"₹",(2*UNITS))
    
elif UNITS<=200:
    REMAINING =UNITS-100
    print ('AMOUNT-',"₹",(2*100)+(REMAINING*3))
    
elif UNITS<=300:
    REMAINING =UNITS-200
    print ('AMOUNT-',"₹",(2*100)+(100*3)+(REMAINING*5))
    
else:
    REMAINING =UNITS-300
    print ('AMOUNT-',"₹",(2*100)+(100*3)+(100*5)+(REMAINING*7))

# ---------------------------------------
#SAMPLE -
#ENTER UNITS-202
#AMOUNT- ₹ 510.0

# ---------------------------------------
#SAMPLE -
#ENTER UNITS-3333
#AMOUNT- ₹ 22231.0


