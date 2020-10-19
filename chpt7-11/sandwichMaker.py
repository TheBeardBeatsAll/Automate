#! python3
import pyinputplus as pyip

prices = {'white': 1, 'wheat': 1.25, 'sourdough': 1.5,
          'chicken': 2, 'turkey': 1.75, 'ham': 2.25, 'tofu': 2.5,
          'cheddar': 1, 'swiss': 1.5, 'mozzarella': 2,
          'mayo': 0.25, 'mustard': 0.3, 'lettuce': 0.4, 'tomato': 0.35}
selection = []
print('Time to make your sandwich')
selection.append(pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True))

selection.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True))

if pyip.inputYesNo(prompt='Do you want cheese?') == 'yes':
    selection.append(pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))

if pyip.inputYesNo(prompt='Do you want mayo?')[0].lower() == 'y':
    selection.append('mayo')
if pyip.inputYesNo(prompt='Do you want mustard?')[0].lower() == 'y':
    selection.append('mustard')
if pyip.inputYesNo(prompt='Do you want lettuce?')[0].lower() == 'y':
    selection.append('lettuce')
if pyip.inputYesNo(prompt='Do you want tomato?')[0].lower() == 'y':
    selection.append('tomato')

# Get price of sandwich based on selection
quantity = pyip.inputInt('How many of this sandwich do you want? ', min=1)
total = 0
for ingredient in selection:
    total += prices[ingredient]
total *= quantity # Get updated price based on quantity of sandwichs
print('Your total is: ' + str(total))