def comma(list):
    strList = ''
    for i in range(0, len(list)):
        if i == len(list) - 1:
            strList += list[i]
        elif i == len(list) - 2:
            strList += list[i] + ' and '
        else:
            strList += list[i] + ', '
    return strList

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
spoof = ['apples', 'tofu']
print(comma(spoof))