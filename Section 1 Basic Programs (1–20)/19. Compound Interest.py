# ---------------------------------------
# Program 19: Compound Interest
# Description: Calculates compound interest.
# Author: Anugya Agrawal
# ---------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of intrest: "))
time = float(input("Enter time (Year): "))
n = int(input("Enter number of times compounded per year: "))

if principal < 0 or rate < 0 or time < 0:
    print("Invalid Inputs")
elif n <= 0:
    print("NUMBER OF COMPOUNDING TIMES MUST BE GREATER THAN 0")
else:
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = amount - principal

    print("COMPOUND INTEREST -", compound_interest)
    print("TOTAL AMOUNT -", amount)
