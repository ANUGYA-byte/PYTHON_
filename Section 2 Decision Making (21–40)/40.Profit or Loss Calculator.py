# ---------------------------------------
# Program 40: Profit or Loss Calculator
# Description:Calculates profit or loss based on cost price and selling price.
# Author: Anugya Agrawal
#---------------------------------------
COST_PRICE=float(input('ENTER COST PRICE-'))
SELLING_PRICE=float(input('ENTER SELLING PRICE-'))
if COST_PRICE > SELLING_PRICE:
    LOSS=COST_PRICE-SELLING_PRICE
    print("LOSS-Rs",LOSS)
elif COST_PRICE < SELLING_PRICE:
    PROFIT=SELLING_PRICE-COST_PRICE
    print("PROFIT-Rs",PROFIT)
else:
    print(" NO PROFIT AND LOSS")

# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-230
#ENTER SELLING PRICE-44
#LOSS-Rs 186.0
# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-45
#ENTER SELLING PRICE-45
#NO PROFIT AND LOSS
# ---------------------------------------
#SAMPLE -
#ENTER COST PRICE-33
#ENTER SELLING PRICE-333
#PROFIT-Rs 300.0
