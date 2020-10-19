#! python3

def comma(list):
    strList = ''
    # Turn list into a string of form x, y, z, and a
    for i in range(0, len(list)):
        if i == len(list) - 1: # if last element add element to string
            strList += list[i]
        elif i == len(list) - 2: # if 2nd last element add element + ' and '
            strList += list[i] + ' and '
        else: # o/w add element & comma
            strList += list[i] + ', ' 
    return strList

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
spoof = ['apples', 'tofu']
print(comma(spoof))