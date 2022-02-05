#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''
def disemvowel(string_):
    vowels_ = ["a","e","i","o","u","A","E","I","O","U"]
    new_word = []
    for each in string_:
        if each in vowels_:
            new_word.append("")
        else:
            new_word.append(each)
    strVowels = (''.join(new_word))    #CONVERTING AN ARRAY IN TO A STRIN
    print(strVowels)
    return strVowels

'''
Attempt 2

def disemvowel(string_):
    vowels_ = ["a","e","i","o","u"]
    new_word = ""
    for each in string_:
        pass
        if each.lower() in vowels_:
            new_word + ""
        else:
            new_word += each
            continue
    return new_word
disemvowel("aaaThis website is for losers LOL!")
'''


'''
Top voted answer

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


'''
disemvowel("aaaThis website is for losers LOL!")
