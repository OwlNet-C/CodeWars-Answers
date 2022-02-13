#https://www.codewars.com/kata/573d498eb90ccf20a000002a/train/python

'''
Fans of The Wire will appreciate this one. For those that haven't seen the show, 
the Barksdale Organization has a simple method for encoding telephone numbers exchanged via pagers: "Jump to the other side of the 5 on the keypad, and swap 5's and 0's."

Here's a keypad for visualization.

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
Detective, we're hot on their trail! We have a big pile of encoded messages here to use as evidence, 
but it would take way too long to decode by hand. Could you write a program to do this for us?

Write a function called decode(). Given an encoded string of exactly 10 digits,
return the actual phone number in string form. Don't worry about input validation, parenthesis, or hyphens.
'''



def decode(strng):
    empty = ""
    rev = ['9','8','7','6','0']
    forward = ['1','2','3','4','5']
    for each in strng:
        if each in forward:
            ind = forward.index(each)
            empty += rev[ind]
        elif each in rev:
            ind = rev.index(each)
            empty += forward[ind]
    return empty

decode("4103432323")


'''
Top rated answer:
def decode(s):
    return s.translate(str.maketrans("1234567890", "9876043215"))


'''
