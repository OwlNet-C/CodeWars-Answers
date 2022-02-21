#https://www.codewars.com/kata/5d5a7525207a674b71aa25b5/train/python

'''
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
'''
'''
*******************************************************************
************Note FIRST ELEMENT OF EACH ROW IS GOING UP IN 2s. 
1 -> 3: 2.
3 ->7 : 4.
7 -> 13 : 6.
13 -> 21 : 8.
In my soloution i use this pattern to find the first element of the nth row.
From then on i simply finish the row by adding 2 to the first element Ntimes
'''
def odd_row(n):
    arr = []
    form = 0
    for each in range(0,2*n,2):
        form += each
    num_1 = form +1
    for each in range(0,n):
        arr.append(num_1)
        num_1 +=2

    return(arr)


odd_row(19)


'''
Personal favourite answer:
def odd_row(n):
    #To store numbers in row
    row = []
    #Formula for first number in row
    firstnum = (n * (n - 1)) + 1
    #Add first number to row
    row.append(firstnum)
    #While length of row is not equal to n...
    #Because amount of numbers in a row is always equal to row number
    while len(row) != n:
        #Add 2 to the previous number and append to list
        row.append(row[-1] + 2)
        
    return row

'''
