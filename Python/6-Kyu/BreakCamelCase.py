#https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''
def solution(s):
    ans = ""
    for each in s:
        if each.isupper() == True:
            ans += " "
        ans += each
    return(ans)

solution("helloWorld")
solution("hellowWorldMyNameIsJoy")


'''
Personal favourite:

'''
