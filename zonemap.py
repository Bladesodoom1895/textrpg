### make n, s, e, w point to other zone objects to traverse node tree ###

##### Map #####
"""
a1 a2 a3 a4 x = player home
-------------
|  |  |  |  | a4
-------------
|  |X |  |  | b4
-------------
|  |  |  |  | c4
-------------
|  |  |  |  | d4
-------------
"""

import random

class Zone:
    def __init__(self, name: str, solved: bool) -> None:
        self.name = name
        self.solved = solved
        self.description = '',
        self.look = '',
        self.riddle = '',
        self.answer = '',
        self.north = '',
        self.east = '',
        self.south = '',
        self.west = ''


### Zone builder for the map ###

# getting each line from the riddles.txt
with open('riddles.txt', 'r') as r:
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
        zones[l + n] = Zone(name=f'{{l}}{n}', solved=False)
        # pulls last entry in riddle_lines and puts it in zone
        zones[l + n].riddle, zones[l + n].answer = riddle_lines.pop().split(': ')


# a1
zones['a1'].description = "zone a1's description"
zones['a1'].look = "zone a1's look"
zones['a1'].east = 'a2'
zones['a1'].south = 'b1'


# a2
zones['a2'].description = "zone a2's description"
zones['a2'].look = "zone a2's look"
zones['a2'].east = 'a3'
zones['a2'].south = 'b2'
zones['a2'].west = 'a1'

# a3
zones['a3'].description = "zone a2's description"
zones['a3'].look = "zone a3's look"
zones['a3'].east = 'a4'
zones['a3'].south = 'b3'
zones['a3'].west = 'a2'

# a4
zones['a4'].description = "zone a4's description"
zones['a4'].look = "zone a4's look"
zones['a4'].south = 'b4'
zones['a4'].west = 'a3'

# b1
zones['b1'].description = "zone b1's description"
zones['b1'].look = "zone b1's look"
zones['b1'].north = 'a1'
zones['b1'].east = 'b2'
zones['b1'].south = 'c1'

# b2
zones['b2'].description = "zone b2's description"
zones['b2'].look = "zone b2's look"
zones['b2'].north = 'a2'
zones['b2'].east = 'b3'
zones['b2'].south = 'c2'
zones['b2'].west = 'b1'

# b3
zones['b3'].description = "zone b3's description"
zones['b3'].look = "zone b3's look"
zones['b3'].north = 'a3'
zones['b3'].east = 'b4'
zones['b3'].south = 'c3'
zones['b3'].west = 'b2'

# b4
zones['b4'].description = "zone b4's description"
zones['b4'].look = "zone b4's look"
zones['b4'].north = 'a4'
zones['b4'].south = 'c4'
zones['b4'].west = 'b3'

# c1
zones['c1'].description = "zone c1's description"
zones['c1'].look = "zone c1's look"
zones['c1'].north = 'b1'
zones['c1'].east = 'c2'
zones['c1'].south = 'c2'

# c2
zones['c2'].description = "zone c2's description"
zones['c2'].look = "zone c2's look"
zones['c2'].north = 'b2'
zones['c2'].east = 'c3'
zones['c2'].south = 'd2'
zones['c2'].west = 'c1'

# c3
zones['c3'].description = "zone c3's description"
zones['c3'].look = "zone c3's look"
zones['c3'].north = 'b3'
zones['c3'].east = 'c4'
zones['c3'].south = 'd3'
zones['c3'].west = 'c2'

# c4
zones['c4'].description = "zone c4's description"
zones['c4'].look = "zone c4's look"
zones['c4'].north = 'b4'
zones['c4'].south = 'd4'
zones['c4'].west = 'c3'

# d1
zones['d1'].description = "zone d1's description"
zones['d1'].look = "zone d1's look"
zones['d1'].north = 'c1'
zones['d1'].east = 'd2'

# d2
zones['d2'].description = "zone d2's description"
zones['d2'].look = "zone d2's look"
zones['d2'].north = 'c2'
zones['d2'].east = 'd3'
zones['d2'].west = 'd1'

# d3
zones['d3'].description = "zone d3's description"
zones['d3'].look = "zone d3's look"
zones['d3'].north = 'c3'
zones['d3'].east = 'd4'
zones['d3'].west = 'd2'

# d4
zones['d4'].description = "zone d4's description"
zones['d4'].look = "zone d4's look"
zones['d4'].north = 'c4'
zones['d4'].west = 'd3'