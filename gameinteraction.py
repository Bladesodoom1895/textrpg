#### Game Interactivity #####

import sys
from playerenemyclasses import *
from zonemap import *
from gamefunction import *

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print('\n' + "==========================")
    print("What would you like to do?")
    acceptable_actions = {'move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look'}
    print(acceptable_actions)
    action = str(input("> "))
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = str(input("> "))
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action.lower() in ['examine', 'look', 'inspect', 'interact']:
        player_examine()


def player_move():
    ask = "where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to " + destination[0] + ".")
    myPlayer.location = destination[0]
    main_game_loop()


def player_examine():
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already exhausted the zone.")
        prompt()
    else:
        print('You can trigger a puzzle here.')
        print('Would you like to solve the puzzle?')
        print('(yes or no)')
        answer = input("> ")
        if answer == 'yes':
            pass #print puzzle
        else:
            prompt()