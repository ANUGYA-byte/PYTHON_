# ---------------------------------------
# Program 19: Compound Interest
# Description: Calculates compound interest.
# Author: Anugya Agrawal
# ---------------------------------------

principal = float(input("ENTER PRINCIPAL AMOUNT: "))
rate = float(input("ENTER RATE OF INTEREST (%): "))
time = float(input("ENTER TIME (YEARS): "))
n = int(input("ENTER NUMBER OF TIMES COMPOUNDED PER YEAR: "))

if principal < 0 or rate < 0 or time < 0:
    print("INVALID INPUT")
elif n <= 0:
    print("NUMBER OF COMPOUNDING TIMES MUST BE GREATER THAN 0")
else:
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = amount - principal

    print("COMPOUND INTEREST -", compound_interest)
    print("TOTAL AMOUNT -", amount)
