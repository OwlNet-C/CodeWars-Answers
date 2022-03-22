#https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.

Valid inputs examples:

Examples of valid inputs:
1.2.3.4
123.45.67.89

Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
'''


def is_valid_IP(strng):
  count = 0
#CHECKING FOR EMPTY STRINGS
  if not strng:
    return False

#Checking for letters and random spaces before and after numbers
  for char in strng:
    if char.isalpha() == True:
      return False
    if char == " ":
      return False
#CHECKING FOR 255 VALUES/NEGATIVE VALUES.
#initialising count variable
  for each in strng.split("."):
    count+=1
    if each[0] == "0" and each != "0": #Check for leading 0s
      return False
    if int(each)>255 or int(each)<0:  #BIGGER THAN 255 CHECK or negative value
      return False

#CHECKING FOR 4 VALUES ENTERED
  if count == 4:   
    return True
  else:
    return False



is_valid_IP('12.34.56 .1')
is_valid_IP('123.045.067.089')

'''
Personal favourite:

'''
