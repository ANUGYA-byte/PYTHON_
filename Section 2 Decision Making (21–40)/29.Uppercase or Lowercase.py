# ---------------------------------------
# Program 29:Uppercase or Lowercase 
# Description:Checks whether a given alphabet is uppercase or lowercase.
# Author: Anugya Agrawal
# ---------------------------------------
ALPHABET=input("Enter the alphabet-")
if len(ALPHABET)==1:
 if  ALPHABET.isupper():
    print(ALPHABET,'UPPERCASE')
 elif ALPHABET.islower():
    print(ALPHABET,'LOWERCASE')
 else:
    print(ALPHABET,'It is NOT ALPHABET')  


# ---------------------------------------
#SAMPLE -
#Enter the alphabet-w
#w LOWERCASE
# ---------------------------------------
#SAMPLE -
#Enter the alphabet-A
#A UPPERCASE
