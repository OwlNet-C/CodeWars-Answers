#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
'''
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
'''

def multiplication_table(size):
    temp = size
    top_row = []
    answer = []
    while temp != 0:
        top_row.append(temp)
        temp -=1
        top_row.sort()
    left_row = top_row    
    count = 0 
    for each in top_row:
        for i in range(0,size):
            answer.append(left_row[i] * each)
    return [answer[i::size] for i in range(size)]

multiplication_table(3)

'''
personal favourite: 

def multiplication_table(size):
    columns = []
    for i in range(1,size+1):
        rows = []
        for j in range(1,size+1):
            rows.append(i*j)
        columns.append(rows)
        
    return columns

'''
