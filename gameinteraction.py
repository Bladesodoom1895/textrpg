# TODO: rework this to function with the zonemap.py and riddles.py changes #

# Warriors Text RPG

import sys
import os
import time
import zonemap
from playerenemyclasses import *


def clear():
    """ An OS agnostic command to clear the screen. """
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(message, delay=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def title_screen():
    clear()
    print('#' * 28)
    print('Welcome to Warriors Text RPG')
    print('#' * 28)
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    title_screen_selections()


def help_menu():
    clear()
    print('#' * 28)
    print('Welcome to Warriors Text RPG')
    print('#' * 28)
    print('- Use  the letters n, s, e, w to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    time.sleep(10)
    title_screen()


##### Title Screen #####
def title_screen_selections():
    while True:
        option = input("> ").lower().strip()
        if option == ("play"):
            setup_game(zonemap)

        elif option== ("help"):
            help_menu()

        elif option == ("quit"):
            sys.exit()
        else:
            input("Unknown selection, try again.")


def setup_game(zonemap):
    clear()

    ##### Name Handling #####
    nameq = "Hello, what's your name?\n"
    typewriter(nameq)
    player_name = input("> ")
    myPlayer.name = player_name

    ##### Job Handling #####
    jobq = "What role do you want to play?\n"
    typewriter(jobq, delay=0.03)
    jobq2 = "(You can play as warrior, priest, or mage)\n"
    typewriter(jobq2, delay=0.03)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    while player_job.lower().strip() not in valid_jobs:
        print('That is not a valid job!')
        player_job = input('> ')
        if player_job.lower().strip() in valid_jobs:
            myPlayer.job = player_job
            print('You are now a ' + player_job + '!\n')

    ##### Player Stats #####
    if myPlayer.job == 'warrior':
        myPlayer.hp = 120
        myPlayer.mp = 20
    elif myPlayer.job == 'mage':
        myPlayer.hp = 40
        myPlayer.mp = 120
    elif myPlayer.job == 'priest':
        myPlayer.hp = 60
        myPlayer.mp = 60
    

    ##### Introduction #####
    question3 = "Welcome, " + player_name + " the " + player_job + '.\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "This is the fantasy world of Erast!\n"
    typewriter(speech1)
    speech2 = "I hope it greets you well!\n"
    typewriter(speech2)
    speech3 = "Just make sure you don't get too lost!\n"
    typewriter(speech3,delay=0.04)
    speech4 = "Hehehe..."
    typewriter(speech4,delay=0.1)
    time.sleep(1)

    clear()
    print('###################')
    print("# Let's Start Now #")
    print('###################')
    main_game_loop()


#### Game Functionality #####
def main_game_loop():
    while myPlayer.game_over is False:
        print_location()
    else:
        time.sleep(5)
        clear()
        title_screen()


#### Game Interactivity #####
def print_location():
    current_zone = zonemap.zones[myPlayer.location]
    print("\n" + ("#" * (4 + len(current_zone.name))))
    print("Current Zone: " + current_zone.name)
    print("#" * (4 + len(current_zone.name)))
    print("\n" + current_zone.description)
    prompt()


def prompt():
    print('\n' + "=" * 25)
    print("What would you like to do?")
    acceptable_actions = {'move', 'quit', 'look'}
    print(acceptable_actions)
    while True:
        action = input("> ").lower().strip()
        if action == 'quit':
            sys.exit()
        elif action in ['move']:
            player_move()
        elif action in ['look']:
            player_look()
        else:
            input("Unknown selection, try again.")

def player_move():
    """ask player where they would like to move out of the directions
    if not a valid direction ask again, if a valid direction, check
    if the direction has a zone next to it, if so send the new location
    to movement handler, if not tell them they can't move there and ask
    again"""
    dest = input("Where would you like to move to? \n" ">").strip().lower()

    while dest not in ['n','e','s','w']:
        print("Not a valid location to move.")
        dest = input("Where would you like to move to? \n" ">").strip().lower()

    while True:
        new_location = getattr(zonemap.zones[myPlayer.location], dest)
        if new_location[0] == '':
            print("Invalid move")
            player_move()
        else:
            movement_handler(new_location)
            

def movement_handler(dest):
    print(dest)
    print("You have moved to " + dest + ".")
    myPlayer.location = dest
    main_game_loop()


def player_look():
    print(zonemap.zones[myPlayer.location].look)

    if zonemap.zones[myPlayer.location].solved == True:
        print("You have already exhausted the zone.")
        prompt()
    else:
        print('You can trigger a puzzle here.')
        print('Would you like to solve the puzzle?')
        print('(yes or no)')
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            riddles()
        elif answer.lower().lower().strip() == 'no':
            prompt()
        else:
            print('That is not valid input')
            player_look()


def riddles():
    print(zonemap.zones[myPlayer.location].riddle)
    time.sleep(2)
    ask = 'What is your answer.\n'
    typewriter(ask, delay=0.03)

    player_ans = input('> ')

    if player_ans.lower().strip() == zonemap.zones[myPlayer.location].answer:
        print("Congratulations that is correct!")
        zonemap.zones[myPlayer.location].solved = True
        time.sleep(4)
        win_condition()
    else:
        print('That is incorrect, try again.')
        riddles()


def win_condition():
    all_solved = True
    for zone in zonemap.zones.values():
        if zone.solved == False:
            all_solved = False
        main_game_loop()

    if all_solved == True:
        print('Congratulations you have won!')
        time.sleep(10)
        myPlayer.game_over = True
        main_game_loop()


title_screen()
