#https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
'''
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''

def get_grade(s1, s2, s3):
  avg = (s1+s2+s3)/3
  if 90 <= avg <= 100:
    return 'A'
  elif 80 <= avg < 90:
    return 'B'
  elif 70 <= avg < 80:
    return 'C'
  elif 60 <= avg < 70:
    return 'D'
  elif 0 <= avg < 60:
    return 'F'

get_grade(95, 90, 93)

'''
Personal favourite:

def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'


'''
