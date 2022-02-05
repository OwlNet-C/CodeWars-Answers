#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
'''
from dataclasses import replace

def fake_bin(x):
    binary_value = ""
    for each in x:
        print(each)
        conv = int(each)
        if conv >= 5:
            binary_value +="1"
        elif conv < 5:
            binary_value += "0"
    print(binary_value)
    return binary_value


'''
Top rated answer 

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


'''

fake_bin("1247830537537")
