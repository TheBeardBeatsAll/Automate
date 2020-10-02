import re

def strip(text):
    stripStartRegex = re.compile(r'(^\s*)')
    stripEndRegex = re.compile(r'(\s*$)')

    textStartStripped = stripStartRegex.sub('', text)
    textStripped = stripEndRegex.sub('', textStartStripped)

    return textStripped

print(strip(' testing 123   '))