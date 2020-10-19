#! python3

import zombiedice, random

class randomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # 50/50 chance it will roll again:
        results = zombiedice.roll() # first roll
        while results and random.randint(0, 1) == 0:
            results = zombiedice.roll()

# Zombie stops at 2 brains each turn
class stopAt2Brains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        results = zombiedice.roll()
        brains = 0
        while results:
            brains += results['brains']

            if brains < 2:
                results = zombiedice.roll()
            else:
                break

# Zombie stops at 2 shotguns each turn
class stopAt2Shotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        results = zombiedice.roll()
        shotguns = 0
        while results:
            shotguns += results['shotgun']

            if shotguns < 2:
                results = zombiedice.roll()
            else:
                break

# Zombie randomly decides between 1 & 4 rolls & stops at 2 brains each turn 
class oneToFourStopAt2Shotgun:
    def __init__(self, name):
        self.name = name
        

    def turn(self, gameState):
        results = zombiedice.roll()
        turnAmount = random.randint(1, 4)
        shotguns = 0
        turnNum = 0
        while results and turnNum < turnAmount:
            shotguns += results['shotgun']

            if shotguns < 2:
                results = zombiedice.roll()
                turnNum += 1
            else:
                break

# Zombie stops when more shotguns than brains
class moreShotgunsThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        results = zombiedice.roll()
        brains = 0
        shotguns = 0
        while results:
            brains += results['brains']
            shotguns += results['shotgun']

            if shotguns <= brains:
                results = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    randomZombie(name='Random'),
    stopAt2Brains(name='StopsAt2Brains'),
    stopAt2Shotguns(name='StopsAt2Shotguns'),
    oneToFourStopAt2Shotgun(name='1to4StopsAt2Shotgun'),
    moreShotgunsThanBrains(name='MoreShotgunThanBrains'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)