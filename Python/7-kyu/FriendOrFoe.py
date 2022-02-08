#https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.
'''
def friend(x):
  temp = []
  for each in x:
    if len(each) == 4:
      temp.append(each)
  return temp
      
    

friend(["Ryan", "Kieran", "Mark",])

'''
Top Rated answer:

def friend(x):
    return [f for f in x if len(f) == 4]

Personal note answer:

def friend(x):
    return filter(lambda name: len(name) == 4, x)

'''
