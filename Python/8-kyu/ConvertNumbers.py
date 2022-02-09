#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

'''
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

348597 => [7,9,5,8,4,3]

'''
def digitize(n):
    temp = []
    for each in list(str(n))[::-1]:
        temp.append(int(each))
    return temp


digitize(35231)
'''
Top Rated Answer :

def digitize(n):
    return map(int, str(n)[::-1])

Clever Answer:

'''
