#https://www.codewars.com/kata/5601409514fc93442500010b/train/python

'''
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!
'''
def better_than_average(class_points, your_points):
    tot = 0
    for each in class_points:
        tot += each
    avg = (tot / (len(class_points)))
    if avg < your_points:
        return True
    else:
        return False

better_than_average([2, 3], 5)
'''
Top rated answer:
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

Personal favourite: 
def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

'''
