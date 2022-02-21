#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''
def array_diff(a, b):
    arr = []
    for each in a:
        if each in b:
            continue
        arr.append(each)
    return(arr)

    
    #your code here


array_diff([1,2], [1]) #c        2
array_diff([1,2,3], [1, 2]) #C   3
array_diff([1,2,2], [])  # C     1 2 2
array_diff([], [1,2])    #C      []
array_diff([1,2,3], [1, 2]) # C  3

'''
Personal favourite:

def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a

'''
