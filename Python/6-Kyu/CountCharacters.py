#https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
'''
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''


def count(string):
  tmp = {}
  for each in string:
    tmp[each] = 0

  for each in string:
    tmp[each] +=1
  return tmp


count('aba')


'''
Personal favourite:

from collections import Counter

def count(string):
    return Counter(string)

'''
