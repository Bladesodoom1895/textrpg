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

ZONENAME = 'name'
DESCRIPTION = 'description'
EXAMINE = 'examine'
RIDDLE = 'riddle'
ANSWER = 'answer'
SOLVED = True
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

zonemap = {
        'a1': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to A1",
            EXAMINE: "Nothing yet",
            RIDDLE: 'I have no legs to dance on, no lungs to breathe. I have no life to live or die, yet do all three. What am I?',
            ANSWER: 'fire',
            SOLVED: False,
            UP: '',
            DOWN: 'b1',
            LEFT: '',
            RIGHT: 'a2',
        },
        'a2': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to A2",
            EXAMINE: "Nothing yet",
            RIDDLE: "I'm at the beginning of time and part of past, present and future. I'm part of history, but not of here and now. In a moment you'll find me, if you know what I am. What am I?",
            ANSWER: "the letter t",
            SOLVED: False,
            UP: '',
            DOWN: 'b3',
            LEFT: 'a1',
            RIGHT: 'a3',
        },
        'a3': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to A3",
            EXAMINE: "Nothing yet",
            RIDDLE: "I can bring tears to your eyes and a smile to your face. I form in an instant and last for a lifetime, but I can be forgotten. What am I?",
            ANSWER: 'a memory',
            SOLVED: False,
            UP: '',
            DOWN: 'b3',
            LEFT: 'a3',
            RIGHT: 'a4',
        },
        'a4': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to A4",
            EXAMINE: "Nothing yet",
            RIDDLE: 'What is harder to catch the faster you run?',
            ANSWER: 'your breath',
            SOLVED: False,
            UP: '',
            DOWN: 'b4',
            LEFT: 'a4',
            RIGHT: '',
        },
        'b1': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to B1",
            EXAMINE: "Nothing yet",
            RIDDLE: "Walk on the living they don't even mumble. Walk on the dead, they mutter and grumble. What are they?",
            ANSWER: 'leaves',
            SOLVED: False,
            UP: 'a1',
            DOWN: 'c1',
            LEFT: '',
            RIGHT: 'b2',
        },
        'b2': {
            ZONENAME: "",
            DESCRIPTION: "This is your home.",
            EXAMINE: "You look around at your wonderful home.",
            SOLVED: True,
            UP: 'a2',
            DOWN: 'c2',
            LEFT: 'b1',
            RIGHT: 'b3'
        },
        'b3': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to B3",
            EXAMINE: "Nothing yet",
            RIDDLE: 'What is it that you can keep after giving it to someone else?',
            ANSWER: 'your word',
            SOLVED: False,
            UP: 'a3',
            DOWN: 'c3',
            LEFT: 'b2',
            RIGHT: 'b4',
        },
        'b4': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to B4",
            EXAMINE: "Nothing yet",
            RIDDLE: 'How many oranges grow on a tree?',
            ANSWER: 'all oranges',
            SOLVED: False,
            UP: 'a4',
            DOWN: 'c4',
            LEFT: 'b3',
            RIGHT: '',
        },
        'c1': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to C1",
            EXAMINE: "Nothing yet",
            RIDDLE: "If I have it, I shouldn't share it, because if I share it, I won't have it. What is it?",
            ANSWER: 'a secret',
            SOLVED: False,
            UP: 'b1',
            DOWN: 'd1',
            LEFT: '',
            RIGHT: 'c2',
        },
        'c2': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to C2",
            EXAMINE: "Nothing yet",
            RIDDLE: 'Light brings me to life, but darkness kills me. What am I?',
            ANSWER: 'a shadow',
            SOLVED: False,
            UP: 'b2',
            DOWN: 'd2',
            LEFT: 'c1',
            RIGHT: 'c3',
        },
        'c3': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to C3",
            EXAMINE: "Nothing yet",
            RIDDLE: 'What loses a head in the morning, but gets it back at night?',
            ANSWER: 'a pillow',
            SOLVED: False,
            UP: 'b3',
            DOWN: 'd3',
            LEFT: 'c2',
            RIGHT: 'c4',
        },
        'c4': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to C4",
            EXAMINE: "Nothing yet",
            RIDDLE: "I'm as a child, a lamb and a simpleton at once. All are born with me, yet few possess me at their moment of death. What am I?",
            ANSWER: 'innocence',
            SOLVED: False,
            UP: 'b4',
            DOWN: 'd4',
            LEFT: 'c3',
            RIGHT: '',
        },
        'd1': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to D1",
            EXAMINE: "Nothing yet",
            RIDDLE: "I'm tall when I'm young and I'm short when I'm old. What am I?",
            ANSWER: 'a candle',
            SOLVED: False,
            UP: 'c1',
            DOWN: '',
            LEFT: '',
            RIGHT: 'd2',
        },
        'd2': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to D2",
            EXAMINE: "Nothing yet",
            RIDDLE: "Every night I'm told what to do and each morning I do what I'm told, yet never do I escape your scold. What am I?",
            ANSWER: 'an alarm clock',
            SOLVED: False,
            UP: 'c2',
            DOWN: '',
            LEFT: 'd1',
            RIGHT: 'd3',
        },
        'd3': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to D3",
            EXAMINE: "Nothing yet",
            RIDDLE: 'I give advice to others, yet I know nothing myself. I am a hitchhiker destined to stay still while others pass by me. What am I?',
            ANSWER: 'a road sign',
            SOLVED: False,
            UP: 'c3',
            DOWN: '',
            LEFT: 'd2',
            RIGHT: 'd4',
        },
        'd4': {
            ZONENAME: "",
            DESCRIPTION: "Welcome to D4",
            EXAMINE: "Nothing yet",
            RIDDLE: "I'm easy to get into, but hard to get out of. What am I?",
            ANSWER: 'trouble',
            SOLVED: False,
            UP: 'c4',
            DOWN: '',
            LEFT: 'd3',
            RIGHT: '',
        }
}