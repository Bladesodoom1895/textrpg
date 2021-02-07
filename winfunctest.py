
solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': True, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

all_solved = True
for value in solved_places.values():
    if value == False:
        all_solved = False

if all_solved == True:
    print('Congratulations you have won!')
    #myPlayer.game_over == True
else:
    #main_game_loop()
    print('Not done yet!')
    pass