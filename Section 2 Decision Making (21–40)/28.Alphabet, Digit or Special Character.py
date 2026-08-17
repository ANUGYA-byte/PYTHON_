# ---------------------------------------
# Program 28: Alphabet, Digit or Special Character
# Description: Determines whether the entered character is an alphabet, digit, or special character.
# Author: Anugya Agrawal
# ---------------------------------------

CHARACTER = input("ENTER THE CHARACTER: ")

if CHARACTER.isdigit():
 print(CHARACTER, "DIGIT")
elif CHARACTER.isalpha():
 print(CHARACTER, "ALPHABET")
else:
 print(CHARACTER, "SPECIAL CHARACTER")

# ---------------------------------------
# SAMPLE 1
# ENTER THE CHARACTER: w
# w ALPHABET
# ---------------------------------------

# ---------------------------------------
# SAMPLE 2
# ENTER THE CHARACTER: 3
# 3 DIGIT
# ---------------------------------------

# ---------------------------------------
# SAMPLE 3
# ENTER THE CHARACTER: @
# @ SPECIAL CHARACTER

# ---------------------------------------

