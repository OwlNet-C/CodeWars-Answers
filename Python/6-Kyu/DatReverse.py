#https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
'''
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
'''


data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
#lookLike [1,0,1,0,1,0,1,0,      0,0,0,0,1,1,1,1,      0,0,0,0,0,0,0,0,      1,1,1,1,1,1,1,1]

def data_reverse(data):
    store1 = []
    place = 0
    for each in range(0,len(data)+8, 8):
        store1.append(data[place:each])
        place = each
    
    store2 = store1[::-1]
    answer = []
    
    for each in store2:
        answer += each
        
    return answer

data_reverse(data1)

