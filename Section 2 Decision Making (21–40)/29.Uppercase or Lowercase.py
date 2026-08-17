# ---------------------------------------
# Program 29:Uppercase or Lowercase 
# Description:Checks whether a given alphabet is uppercase or lowercase.
# Author: Anugya Agrawal
# ---------------------------------------
ALPHABET=input("ENTER THE  ALPHABET-")
if  ALPHABET.isupper():
    print(ALPHABET,'UPPERCASE')
elif ALPHABET.islower():
    print(ALPHABET,'LOWERCASE')
else:
    print(ALPHABET,'IT IS NOT ALPHABET')  


# ---------------------------------------
#SAMPLE -
#ENTER THE  ALPHABET-w
#w LOWERCASE
# ---------------------------------------
#SAMPLE -
#ENTER THE  ALPHABET-A
#A UPPERCASE
