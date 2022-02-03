#https://www.codewars.com/kata/54edbc7200b811e956000556/train/python

'''
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

For example,
'''
array1 = [True,  True,  True,  False,
         True,  True,  True,  True ,
        True,  False, True,  False,
        True,  False, False, True ,
         True,  True,  True,  True ,
        False, False, True,  True]

def count_sheeps(sheep):
    Tcounter = 0
    for each in sheep:
        if each == True:
            Tcounter +=1
    print(Tcounter)
    return Tcounter


#COUNT TRUE AND FALSE BASICALLY
count_sheeps(array1)

#Top voted answer
'''
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
'''
