# Warriors Text RPG
# Dalas Neff :D

import cmd, textwrap, sys, os, time, random
from gameinteraction import *

##### Title Screen #####
def title_screen_selections():
    option = str(input("> "))
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = str(input("> "))
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('cls')
    print('############################')
    print('Welcome to Warriors Text RPG')
    print('############################')
    print('          - Play -          ')
    print('          - Help -          ')
    print('          - Quit -          ')
    title_screen_selections()


def help_menu():
    print('############################')
    print('Welcome to Warriors Text RPG')
    print('############################')
    print('- Use up, down, left, right to move')
    print('- Type your commands to do them')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    title_screen_selections()


title_screen()