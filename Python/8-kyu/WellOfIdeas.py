#https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python

'''
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', 
if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

'''

def well(x):
  print("TRY")
  cg = []
  for each in x:
    if each == 'good':
      cg.append(each)
  if (len(cg)) in (1,2):
    return "Publish!"
  elif (len(cg) > 2):
    return "I smell a series!"
  elif len(cg) == 0:
    return "Fail!"


well(['bad', 'bad', 'bad'])
well(['good', 'bad', 'bad', 'bad', 'bad'])
well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'])

'''
Top rated answer:
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'



Personal favorite :
def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
'''
