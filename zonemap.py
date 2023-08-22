#### TODO: rework this into a class ####

""" make n, s, e, w point to other zone objects
to traverse node tree"""

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


class Zone:
    def __init__(self, name: str) -> None:
        self.name = name


### Zone builder for the map ###
letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3', '4']
zones = {}

for l in letters:
    for n in numbers:
        zones[l + n] = Zone(name=f"This is the name for zone {l}{n}")
