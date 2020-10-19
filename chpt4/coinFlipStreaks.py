#! python3

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    randomList = []
    for listEntry in range(100):
        if random.randint(0,1) == 1:
            randomList.append('H')
        else:
            randomList.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    counterH, counterT = 0, 0
    for flip in range(100):
        if randomList[flip] == 'H':
            counterH += 1
            counterT = 0
        else:
            counterT += 1
            counterH = 0
        if counterH == 6 or counterT == 6:
            numberOfStreaks +=1
            counterH, counterT = 0, 0
            
print('Chance of streak: %s%%' % (numberOfStreaks/100))