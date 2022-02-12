#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
  temp = ""
  counter = 0
  for each in s:
      counter +=1
      if counter == 1:
          temp += each.upper()
      elif counter > 1:
          temp += "-" + each.upper()
      temp += each.lower() * (counter-1)
  return temp
accum("ZpglnRxqenU")

'''
Top rated answer:
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

Personal favourite: 
def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]

'''
