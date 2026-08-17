# ---------------------------------------
# Program 19: Compound Interest
# Description: Calculates compound interest using principal, rate, and time.
# Author: Anugya Agrawal
# ---------------------------------------

principal = float(input("ENTER PRINCIPAL AMOUNT: "))
rate = float(input("ENTER RATE OF INTEREST: "))
time = float(input("ENTER TIME (YEAR): "))
n_time = int(input("ENTER NUMBER OF TIMES INTEREST IS COMPOUNDED PER YEAR: "))

amount = principal * (1 + rate / (100 * n_time)) ** (n_time * time)
compound_interest = amount - principal

print("COMPOUND INTEREST -", compound_interest)

# ---------------------------------------
# SAMPLE INPUT-
# ENTER PRINCIPAL AMOUNT: 2000
# ENTER RATE OF INTEREST: 4
# ENTER TIME (YEAR): 2
# ENTER NUMBER OF TIMES INTEREST IS COMPOUNDED PER YEAR: 4
# ---------------------------------------
# SAMPLE OUTPUT-
# COMPOUND INTEREST - 165.71341125616027
# ---------------------------------------
