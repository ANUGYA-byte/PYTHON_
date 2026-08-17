# ---------------------------------------
# Program 27: Vowel or Consonant
# Description: Checks whether a given alphabet character is a vowel or consonant.
# Author: Anugya Agrawal
# ---------------------------------------

alphabet = input("ENTER THE ALPHABET: ")

if alphabet.lower() in "aeiou":
    print(alphabet, "VOWEL")
else:
    print(alphabet, "CONSONANT")

# ---------------------------------------
# SAMPLE INPUT-
# ENTER THE ALPHABET: W
#
# SAMPLE OUTPUT-
# W CONSONANT
#
# ---------------------------------------
# SAMPLE INPUT-
# ENTER THE ALPHABET: E
#
# SAMPLE OUTPUT-
# E VOWEL
# ---------------------------------------
