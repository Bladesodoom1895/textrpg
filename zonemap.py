##### Map #####
"""
        N
    a1 a2 a3 a4 x = player home
    -------------
    |  |  |  |  | a4
    -------------
    |  |X |  |  | b4
W   -------------     E
    |  |  |  |  | c4
    -------------
    |  |  |  |  | d4
    -------------
        S
"""

import random

DEBUG = False

class Zone:
    def __init__(self, name: str, solved: bool) -> None:
        self.name = name
        self.solved = solved
        self.description = '',
        self.look = '',
        self.riddle = '',
        self.answer = '',
        self.n = '',
        self.e = '',
        self.s = '',
        self.w = ''


### Zone builder for the map ###

# getting each line from the riddles.txt
with open('riddles.txt', 'r', encoding="utf8") as r:
    riddle_lines = r.readlines()

# cleaning up lines to remove empty lines and white space, list comprehension is kick ass
riddle_lines = [i.strip() for i in riddle_lines if i.strip() != ""]

# random sort
random.shuffle(riddle_lines)

letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3', '4']
zones = {}

for l in letters:
    for n in numbers:
        zones[l + n] = Zone(name=f'{l}{n}', solved=False)
        # pulls last entry in riddle_lines and puts it in zone
        zones[l + n].riddle, zones[l + n].answer = riddle_lines.pop().split(': ')



# a1
zones['a1'].description = "zone a1's description"
zones['a1'].look = "zone a1's look"
zones['a1'].e = 'a2'
zones['a1'].s = 'b1'


# a2
zones['a2'].description = "zone a2's description"
zones['a2'].look = "zone a2's look"
zones['a2'].e = 'a3'
zones['a2'].s = 'b2'
zones['a2'].w = 'a1'

# a3
zones['a3'].description = "zone a3's description"
zones['a3'].look = "zone a3's look"
zones['a3'].e = 'a4'
zones['a3'].s = 'b3'
zones['a3'].w = 'a2'

# a4
zones['a4'].description = "zone a4's description"
zones['a4'].look = "zone a4's look"
zones['a4'].s = 'b4'
zones['a4'].w = 'a3'

# b1
zones['b1'].description = "zone b1's description"
zones['b1'].look = "zone b1's look"
zones['b1'].n = 'a1'
zones['b1'].e = 'b2'
zones['b1'].s = 'c1'

# b2
zones['b2'].description = "zone b2's description"
zones['b2'].look = "zone b2's look"
zones['b2'].n = 'a2'
zones['b2'].e = 'b3'
zones['b2'].s = 'c2'
zones['b2'].w = 'b1'

# b3
zones['b3'].description = "zone b3's description"
zones['b3'].look = "zone b3's look"
zones['b3'].n = 'a3'
zones['b3'].e = 'b4'
zones['b3'].s = 'c3'
zones['b3'].w = 'b2'

# b4
zones['b4'].description = "zone b4's description"
zones['b4'].look = "zone b4's look"
zones['b4'].n = 'a4'
zones['b4'].s = 'c4'
zones['b4'].w = 'b3'

# c1
zones['c1'].description = "zone c1's description"
zones['c1'].look = "zone c1's look"
zones['c1'].n = 'b1'
zones['c1'].e = 'c2'
zones['c1'].s = 'c2'

# c2
zones['c2'].description = "zone c2's description"
zones['c2'].look = "zone c2's look"
zones['c2'].n = 'b2'
zones['c2'].e = 'c3'
zones['c2'].s = 'd2'
zones['c2'].w = 'c1'

# c3
zones['c3'].description = "zone c3's description"
zones['c3'].look = "zone c3's look"
zones['c3'].n = 'b3'
zones['c3'].e = 'c4'
zones['c3'].s = 'd3'
zones['c3'].w = 'c2'

# c4
zones['c4'].description = "zone c4's description"
zones['c4'].look = "zone c4's look"
zones['c4'].n = 'b4'
zones['c4'].s = 'd4'
zones['c4'].w = 'c3'

# d1
zones['d1'].description = "zone d1's description"
zones['d1'].look = "zone d1's look"
zones['d1'].n = 'c1'
zones['d1'].e = 'd2'

# d2
zones['d2'].description = "zone d2's description"
zones['d2'].look = "zone d2's look"
zones['d2'].n = 'c2'
zones['d2'].e = 'd3'
zones['d2'].w = 'd1'

# d3
zones['d3'].description = "zone d3's description"
zones['d3'].look = "zone d3's look"
zones['d3'].n = 'c3'
zones['d3'].e = 'd4'
zones['d3'].w = 'd2'

# d4
zones['d4'].description = "zone d4's description"
zones['d4'].look = "zone d4's look"
zones['d4'].n = 'c4'
zones['d4'].w = 'd3'


if DEBUG:
    new_zones = []
    for letter in letters:
        for number in numbers:
            new_zones.append(f"{letter}{number}")

    for location in new_zones:
        if location != "b2":
            zones[location].solved = True

    for zone in zones.values():
        print(zone.name, zone.solved)