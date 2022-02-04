#https://www.codewars.com/kata/5748a883eb737cab000022a6/train/python

'''
Ahoy Matey!
Welcome to the seven seas.
You are the captain of a pirate ship.
You are in battle against the royal navy.
You have cannons at the ready.... or are they?
Your task is to check if the gunners are loaded and ready, if they are: Fire!
If they aren't ready: Shiver me timbers!
Your gunners for each test case are 4 or less.
When you check if they are ready their answers are in a dictionary and will either be: aye or nay
Firing with less than all gunners ready is non-optimum (this is not fire at will, this is fire by the captain's orders or walk the plank, dirty sea-dog!)
If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!
'''
def cannons_ready(gunners):
    ayetemp = 0
    for key,value in gunners.items():
        if value == 'aye':
            ayetemp +=1
    if ayetemp == len(gunners):
        return ("Fire!")
    else:
        return ("Shiver me timbers!")
'''
IMPORTANT LESSON ABOUT DICTIONARIES, THEY HAVE THEIR OWN WAY IN WHICH YOU HAVE TO ITERATE THROUGH WITH FOR LOOPS ETC.
Often have to split them in to their keys and values and use the .items(), method to correctly itterate them

len(dictionary) Will give us the NUMBER of entries in a dictionary 
when i was using len(key) it was giving the length of the wwords (character count) of each individual word
'''



a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}

print(type(a))

cannons_ready(a)
cannons_ready(b)

'''
Top rated answer

def cannons_ready(gunners):
  return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'

'''


