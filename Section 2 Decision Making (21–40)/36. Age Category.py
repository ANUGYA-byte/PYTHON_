# ---------------------------------------
# Program 36: Age Category 
# Description:— Determines a person's age category based on their age.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------

AGE=int(input('Enter your age-'))

if AGE<=10:
    print ("AGE-",AGE, 'GRADE- A')
    
elif 10<AGE<=20:
    print ("AGE-",AGE, 'GRADE- B')

elif 20<AGE<=30:
    print ("AGE-",AGE, 'GRADE- C')

elif 30<AGE<=40:
    print ("AGE-",AGE, 'GRADE- D')

elif 40<AGE<=50:
    print ("AGE-",AGE, 'GRADE- E')
    
elif AGE>50:
    print ("AGE-",AGE, 'GRADE- F')


# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-22
#AGE- 22 GRADE- C

# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-44
#AGE- 44 GRADE- E


