# ---------------------------------------
# Program 33: Income Tax Calculator
# Description:Calculates income tax based on the given annual income and applicable tax rules.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------


INCOME=float(input('ENTER YOUR INCOME-'))
if INCOME<=400000:
    TAX=0
    print ('TAX-',"₹",TAX)
    
elif 400000<INCOME<=800000:
    TAX=5/100*INCOME
    print ('TAX-',"₹",TAX)

elif 800000<INCOME<=1200000:
    TAX=10/100*INCOME
    print ('TAX-',"₹",TAX)

elif 1200000<INCOME<=1600000:
    TAX=15/100*INCOME
    print ('TAX-',"₹",TAX)

elif 1600000<INCOME<=2000000:
    TAX=20/100*INCOME
    print ('TAX-',"₹",TAX)

elif 2000000<INCOME<=2400000:
    TAX=25/100*INCOME
    print ('TAX-',"₹",TAX)

elif 2400000<INCOME<=2800000:
    TAX=30/100*INCOME
    print ('TAX-',"₹",TAX)

else:
    TAX=35/100*INCOME
    print ('TAX-',"₹",TAX)
# ---------------------------------------
#SAMPLE -
#ENTER YOUR INCOME-1287622
#TAX- ₹ 193143.3

# ---------------------------------------
#SAMPLE -
#ENTER YOUR INCOME-222222
#TAX- ₹ 0

