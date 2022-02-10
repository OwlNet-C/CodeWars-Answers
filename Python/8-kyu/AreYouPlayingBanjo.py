#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

'''
def are_you_playing_banjo(name):
  lower = name.lower()
  for each in lower:
    if each[0] == "r":
      return name + " plays banjo"
    else:
      return name + " does not play banjo" 

are_you_playing_banjo("martin")

'''
Top Rated Answer :

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

Personal Favourite : 
  def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

'''
