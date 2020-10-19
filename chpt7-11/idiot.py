#! python3

import pyinputplus as pyip

# Keep going until user types no
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break
    
print('Thank you. Have a nice day.')