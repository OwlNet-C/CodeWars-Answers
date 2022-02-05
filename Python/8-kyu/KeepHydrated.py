#https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python

'''
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:
'''
import math

def litres(time):
    temp = float(time)
    ans = math.floor(0.5 * temp)
    return ans

litres("1.4")

'''
IN MY DEFENCE I DID TRY THIS ORIGINALLY BUT I FORGOT TO DO INT()
Top  voted answer 

def litres(time):
    return int(time/2)

'''
