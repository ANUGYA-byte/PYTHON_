# ---------------------------------------
# Program 19: Compound Interest
# Description: Calculates compound interest.
# Author: Anugya Agrawal
# ---------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (Year): "))
n = int(input("Enter number of times compounded per year: "))

if principal < 0 or rate < 0 or time < 0:
    print("Invalid Inputs")
elif n <= 0:
    print("Number of compounding time must be greater than 0")
else:
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = amount - principal

    print("Compound Interest:", compound_interest)
    print("Total Amount -", amount)
# ---------------------------------------
# SAMPLE INPUT-
'''
Enter principal amount: 2300
Enter rate of intrest: 3
Enter time (Year): 4
Enter number of times compounded per year: 2
'''
# ---------------------------------------
# SAMPLE INPUT-
'''Compound Interest: 290.9329491692042
Total Amount - 2590.932949169204'''
