import sys

def collatz(number):
    if number % 2 == 0: 
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try: # Take input & pass number through function until it equals 1
        print('Enter number:')
        number = int(input())
        while number != 1:
            number = collatz(number)
        sys.exit()
    except ValueError:
        print('Invalid input (Must be an integer)\n')