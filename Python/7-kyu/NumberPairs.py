#https://www.codewars.com/kata/563b1f55a5f2079dc100008a/train/python
'''
In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.

Note: Both arrays have the same dimensions.

Example:

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
'''
a = [13, 64, 15, 17, 88]
b = [23, 14, 53, 17, 80]

def get_larger_numbers(a, b):
  count = 0
  empty = []
  for each in a and b:
    if a[count] > b[count]:
      empty.append(a[count])
    elif b[count]>a[count]:
      empty.append(b[count])
    else:
      empty.append(a[count])
    count +=1
  return(empty

get_larger_numbers(a, b)

'''
Personal favourite:
def get_larger_numbers(a, b):
    return [max(x, y) for x, y in zip(a, b)]

def get_larger_numbers(a, b):
    return map(max, a, b)


'''
