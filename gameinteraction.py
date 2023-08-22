# TODO: rework this to function with the zonemap.py and riddles.py changes #

# Warriors Text RPG

import sys
import os
import time
import re
import cmd
import textwrap
import random
import zonemap
from playerenemyclasses import *
# Warriors Text RPG


def title_screen():
    os.system('cls')
    print('#' * 28)
    print('Welcome to Warriors Text RPG')
    print('#' * 28)
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    title_screen_selections()


def help_menu():
    os.system('cls')
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
        option = str(input("> "))
        if option.lower().strip() == ("play"):
            setup_game(zonemap)

        elif option.lower().strip() == ("help"):
            help_menu()

        elif option.lower().strip() == ("quit"):
            sys.exit()

        else:
            print("Unknow selection try again.")
            title_screen_selections()


def setup_game(zonemap):
    os.system('cls')

    #### Need to initialize all zones ####
    #### Randomly assign riddles and answers to zones ####

    ##### Name Handling #####
    nameq = "Hello, what's your name?\n"
    for character in nameq:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    ##### Job Handling #####
    jobq = "What role do you want to play?\n"
    jobq2 = "(You can play as warrior, priest, or mage)\n"
    for character in jobq:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in jobq2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
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
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't get too lost!\n"
    speech4 = "Hehehe..."
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1)

    os.system('cls')
    print('###################')
    print("# Let's Start Now #")
    print('###################')
    main_game_loop()


#### Game Functionality #####
def main_game_loop():
    while myPlayer.game_over is False:
        print_location()
        prompt()
    else:
        time.sleep(5)
        os.system('cls')
        quit()


#### Game Interactivity #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location]['Description'] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print('\n' + "=" * 25)
    print("What would you like to do?")
    acceptable_actions = {'move', 'quit', 'look'}
    print(acceptable_actions)
    action = str(input("> "))
    while action.lower().strip() not in acceptable_actions:
        print("Unknown action, try again.\n")
        prompt()

    if action.lower().strip() == 'quit':
        sys.exit()

    elif action.lower().strip() in ['move']:
        player_move()

    elif action.lower().strip() in ['look']:
        player_examine()


def player_move():
    ask = "Where would you like to move to?\n"
    options = ['n', 's', 'e', 'w']

    while True:
        print(options)
        dest = input(ask).lower().strip()

        if dest in options:
            destination = zonemap[myPlayer.location][dest]
            if destination == '':
                print("Sorry, you can't move there.")
            else:
                movement_handler(destination)
                break
        else:
            print("Please enter a valid direction.")


def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    main_game_loop()


def player_examine():
    print(zonemap[myPlayer.location]['Look'])
    if zonemap[myPlayer.location]['Solved'] == True:
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
            player_examine()


def riddles():
    print(zonemap[myPlayer.location]['Riddle'])
    time.sleep(2)
    ask = 'What is your answer.\n'
    for char in ask:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    player_ans = input('> ')

    if player_ans.lower().strip() == zonemap[myPlayer.location]['Answer']:
        print("Congratulations that is correct!")
        zonemap[myPlayer.location]['Solved'] = True
        time.sleep(4)
        win_condition(zonemap)
    else:
        print('That is incorrect, try again.')
        riddles()


def win_condition(zonemap):
    all_solved = True
    for value in zonemap.values():
        if value['Solved'] == False:
            all_solved = False

    if all_solved == True:
        print('Congratulations you have won!')
        time.sleep(10)
        myPlayer.game_over == True
        title_screen()
    else:
        main_game_loop()


title_screen()
