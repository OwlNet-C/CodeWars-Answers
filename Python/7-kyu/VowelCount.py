#https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

'''
def get_count(sentence):
  count =0
  vowl = ['a','e','i','o','u']
  for each in sentence:
    if each in vowl:
      count +=1
  return count    

get_count("Should count all vowels")

'''
Top rated answer:
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

Personal favourite: 
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels

'''
