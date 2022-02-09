#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

'''
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

Example
'''
def sum_array(arr):
    if arr == None or len(arr) == 1 :
        return 0
    elif arr == []:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)


sum_array([6, 2, 1, 8, 10])

'''
Top Rated Answer :

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

Clever Answer:

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

'''
