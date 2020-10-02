import re

def passwordStrength(password):

    eightCharsLongRegex = re.compile(r'[\w\d\s\W\D\S]{8,}')
    upperCaseRegex = re.compile(r'[A-Z]')
    lowerCaseRegex = re.compile(r'[a-z]')
    oneDigitRegex = re.compile(r'\d')
    
    if not eightCharsLongRegex.search(password):
        return False
    elif not upperCaseRegex.search(password):
        return False
    elif not lowerCaseRegex.search(password):
        return False
    elif not oneDigitRegex.search(password):
        return False

    return True
    
print(passwordStrength('a&Dsas9$_'))