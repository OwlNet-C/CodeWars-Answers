#https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
import operator

def order(sentence):
  word = sentence.split(" ")
  num = ['1','2','3','4','5','6','7','8','9','0']
  emp = []
  fin = ""
  for each in word:
    for x in each:
      if x in num:
        emp.append(x)
        print(emp)
        print(word)

  dic = dict(zip((word),(emp)))
  sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
  for x,y in sorted_x:
    fin += (x + " ") 
  return fin[:-1]


order("4of Fo1r pe6ople g3ood th5e the2")


'''
Personal favourite:

def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

'''
