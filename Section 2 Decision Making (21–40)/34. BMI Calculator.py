# ---------------------------------------
# Program 34: BMI Calculator 
# Description:Calculates Body Mass Index (BMI) using a person's weight and height.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------


WEIGHT=float(input('ENTER YOUR WEIGHT IN kg-'))
HEIGHT=float(input('ENTER YOUR HEIGHT IN m-'))
BMI=WEIGHT/(HEIGHT**2)
if HEIGHT <= 0 or WEIGHT <= 0:
    print("INVALID INPUT")
else:
 BMI = WEIGHT / (HEIGHT ** 2)
 if BMI<=18.5:
    print ("BMI-",BMI, 'STATUS-UNDERWEIGHT')
    
 elif 18.5<BMI<=24.9:
    print ("BMI-",BMI, 'STATUS-NORMALWEIGHT')

 elif 24.9<BMI<=29.9:
    print ("BMI-",BMI, 'STATUS-OVERWEIGHT',)

 elif BMI>29.9:
    print ("BMI-",BMI, 'STATUS-OBESITY')


# ---------------------------------------
#SAMPLE -
#ENTER YOUR WEIGHT IN kg-60
#ENTER YOUR HEIGHT IN m-1.70
#BMI- 20.761245674740486 STATUS-NORMALWEIGHT

# ---------------------------------------
#SAMPLE -
#ENTER YOUR WEIGHT IN kg-70
#ENTER YOUR HEIGHT IN m-1.70
#BMI- 26.643598615916957 STATUS-OVERWEIGHT

