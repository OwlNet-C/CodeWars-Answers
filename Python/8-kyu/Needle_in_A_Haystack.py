#https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

'''
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
should return "found the needle at position 5" (in COBOL "found the needle at position 6")
'''
def find_needle(haystack):
  for each in haystack:
    if each == "needle":
      inde = haystack.index(each)
  return "found the needle at position {}" .format(inde)
    

find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])

'''
Top Rated answer:

def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

Personal note answer:


'''
