#https://www.codewars.com/kata/559590633066759614000063/train/python

'''
Story
Ben has a very simple idea to make some profit: he buys something and sells it again.
Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price.
Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.
'''
def min_max(lst):
    temp = []
    temp.append(min(lst))
    temp.append(max(lst))
    return temp




min_max([1,2,3,4,5])

'''
Top Rated answer:

def min_max(lst):
  return [min(lst), max(lst)]

Personal note answer:

def min_max(lst):
  lst.sort()
  tempor = [lst[0],lst[-1]]
  return tempor

'''
