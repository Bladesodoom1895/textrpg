# Warriors Text RPG
# Dalas Neff :D

import sys, os, time, re, cmd, textwrap, random
from playerenemyclasses import *
from zonemap import *
from riddles import *
# Warriors Text RPG


#### Game Functionality #####
def main_game_loop():
    while myPlayer.game_over is False:
        print_location()
        prompt()
    else:
        time.sleep(5)
        os.system('cls')
        quit()


def setup_game(riddles_dict, zonemap):
    os.system('cls')

    #### Randomly assign riddles and answers to zones ####
    riddle_questions = list(riddles_dict.keys())
    random.shuffle(riddle_questions)

    for i, x in zip(riddle_questions, list(zonemap.keys())):
        zonemap[x]['Riddle'] = i
        zonemap[x]['Answer'] = riddles_dict[i]

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


##### Title Screen #####
def title_screen_selections():
    option = str(input("> "))
    while option.lower().strip() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = str(input("> "))
        if option.lower().strip() == ("play"):
            setup_game(riddles_dict, zonemap)

        elif option.lower().strip() == ("help"):
            help_menu()

        elif option.lower().strip() == ("quit"):
            sys.exit()

        else:
            print("Unknow selection try again.")
            title_screen_selections()


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
    print('#' * 28)
    print('Welcome to Warriors Text RPG')
    print('#' * 28)
    print('- Use  the words north, south, east, west to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    title_screen_selections()


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
    ask = "where would you like to move to?\n"
    options = ['n', 's', 'e', 'w']
    print(options)
    dest = input(ask)
    while dest not in options:
        dest = input(ask)
        if dest.lower().strip() == 'n':
            destination = zonemap[myPlayer.location]['North']
            if destination == '':
                print("Sorry, You can't move there.")
                player_move()
            else:
                movement_handler(destination)

        elif dest.lower().strip() == 's':
            destination = zonemap[myPlayer.location]['South']
            if destination == '':
                print("Sorry, You can't move there.")
                player_move()
            else:
                movement_handler(destination)

        elif dest.lower().strip() == 'w':
            destination = zonemap[myPlayer.location]['West']
            if destination == '':
                print("Sorry, You can't move there.")
                player_move()
            else:
                movement_handler(destination)

        elif dest.lower().strip() == 'e':
            destination = zonemap[myPlayer.location]['East']
            if destination == '':
                print("Sorry, You can't move there.")
                player_move()

            else:
                movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    main_game_loop()


def player_examine():
    print(zonemap[myPlayer.location]['Examine'])
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