#https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string,
the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''
def longest(a1, a2):
    empty = []
    fin = a1 + a2
    for each in fin:
        if each in empty:
            pass
        else:
            empty.append(each)
    empty.sort()
    return ''.join([str(each) for each in empty])

longest("aretheyhere", "yestheyarehere")

'''
Top rated answer:
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

USING THE SET FUNCTION TO GET RID OF REPEATS
'''
