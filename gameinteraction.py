#### Game Interactivity #####

import sys, os, time, re
from playerenemyclasses import *
from zonemap import *

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
    options = ['down', 'south', 'left', 'west', 'right', 'east', 'up', 'north']
    print(options)
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        if destination == '':
            print("Sorry, You can't move there.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        if destination == '':
            print("Sorry, You can't move there.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        if destination == '':
            print("Sorry, You can't move there.")
            dest = input(ask)
        else:
            movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        if destination == '':
            print("Sorry, You can't move there.")
            dest = input(ask)
        else:
            movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    main_game_loop()


def player_examine():
    print(zonemap[myPlayer.location][EXAMINE])
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You have already exhausted the zone.")
        prompt()
    else:
        print('You can trigger a puzzle here.')
        print('Would you like to solve the puzzle?')
        print('(yes or no)')
        answer = input("> ")
        if answer == 'yes':
            riddles()
        elif answer =='no':
            prompt()
        else:
            print('That is not valid input')


#### Game Functionality #####
def main_game_loop():
    while myPlayer.game_over is False:
        print_location()
        prompt()
    else:
        time.sleep(5)
        os.system('cls')
        quit()


def setup_game():
    os.system('cls')

    ##### Name Handling #####
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    ##### Job Handling #####
    question2 = "What role do you want to play?\n"
    question2added = "(You can play as warrior, priest, or mage)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('You are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        print('That is not a valid job!')
        player_job = input('> ')
        if player_job.lower() in valid_jobs:
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


def riddles():
    print(zonemap[myPlayer.location][RIDDLE])
    time.sleep(2)
    ask = 'What is your answer.\n'
    for char in ask:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    player_ans = input('> ')

    if player_ans.lower() == zonemap[myPlayer.location][ANSWER]:
        print("Congratulations that is correct!")
        zonemap[myPlayer.location][SOLVED] = True
        win_condition(zonemap)
    else:
        print('That is incorrect.')
        player_ans = input('> ')


def win_condition(zonemap):
    all_solved = True
    for value in zonemap[SOLVED].values():
        if value == False:
            all_solved = False

    if all_solved == True:
        print('Congratulations you have won!')
        myPlayer.game_over == True
        main_game_loop()
    else:
        main_game_loop()