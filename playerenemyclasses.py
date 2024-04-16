##### Player Class #####
class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


class Mage(Player):
    def __init__(self):
        self.hp = 80
        self.mp = 120


class Warrior(Player):
    def __init__(self):
        self.hp = 120
        self.mp = 80


class Priest(Player):
    def __init__(self):
        self.hp = 100
        self.mp = 100


##### Enemy Class #####
class enemy:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
