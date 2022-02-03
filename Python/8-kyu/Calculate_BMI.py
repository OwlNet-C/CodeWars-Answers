#https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''
def bmi(weight, height):
    x = weight / (height*height)
    if x <= 18.5:
        return "Underweight"
    elif x<= 25.0:
        return "Normal"
    elif x <= 30.0:
        return "Overweight"
    elif x > 30:
        return "Obese"

bmi(50, 1.80)

'''
Top Soloution

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"


'''
