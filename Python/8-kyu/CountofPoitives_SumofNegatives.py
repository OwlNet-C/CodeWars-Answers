#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and 
the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''

from itertools import count

def count_positives_sum_negatives(arr):
    temp = 0
    neg_sum = 0
    prefArray = []
    if arr==[]:
        return prefArray
    for each in arr:
        if each>0:
            temp+=1
        else:
            neg_sum += each
    prefArray.append(temp)
    prefArray.append(neg_sum)
    return prefArray


count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])

#First COUNT of positive numbers
#Second should be SUM of negative

'''
Top rated answer 

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
    
'''    


