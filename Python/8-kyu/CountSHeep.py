#https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
'''
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...".
Input will always be valid, i.e. no negative integers.
'''
def count_sheep(n):
  count = 1
  sent = ""
  if n == 0:
    return sent
  while count < n+1:
    sent += "{} sheep...".format(count)
    print(count)
    count +=1
  return sent
    # your code

count_sheep(3)


'''
Personal favourite:

def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep

'''
