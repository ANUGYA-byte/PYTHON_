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
# ---------------------------------------
# Program 32: Electricity Bill Calculator
# Description: Calculates electricity bill based on units consumed.
# Author: Anugya Agrawal
# ---------------------------------------

units = float(input("ENTER ELECTRICITY UNITS: "))

if units < 0:
    print("INVALID UNITS")

elif units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("ELECTRICITY BILL -", bill)

# ---------------------------------------
#SAMPLE -
#ENTER UNITS-202
#AMOUNT- ₹ 510.0

# ---------------------------------------
#SAMPLE -
#ENTER UNITS-3333
#AMOUNT- ₹ 22231.0


