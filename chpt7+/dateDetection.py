import re

def dateFind(inputDate):
    dateRegex = re.compile(r'((\d{2})/(\d{2})/(\d{4}))')
    print(dateRegex.search(inputDate))
    for groups in dateRegex.findall(inputDate):
        dateValidate(groups[0], int(groups[1]), int(groups[2]), int(groups[3]))

def dateValidate(fullDate, day, month, year):
    month30=[4, 6, 9, 11]
    month31=[1, 3, 5, 7, 8, 10, 12]
    invalid = 'Invalid Date: ' + fullDate
    if month in month31:
        if day > 31:
            print(invalid)
            return False
    elif month in month30:
        if day > 30:
            print(invalid)
            return False
    elif month == 2:
        if year % 4 == 0:
            if day > 29:
                print(invalid)
                return False
        elif year % 100 == 0 and year % 400 == 0:
            if day > 29:
                print(invalid)
                return False
        else:
            if day > 28:
                print(invalid)
                return False
    elif month not in month30 and month not in month31:
        print(invalid)
        return False
    if year < 1000 or year > 2999:
        print(invalid)
        return False
    print('Valid Date: ' + fullDate)

dateFind('23/02/2019 ssdsds 29/02/2019 05/01/2020')