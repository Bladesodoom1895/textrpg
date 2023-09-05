# from zonemap import *

# # for zone in zones.values():
# #     print(zone.name, zone.solved)


# def win_condition():
#     all_solved = True
#     for zone in zones.values():
#         if zone.solved == False:
#             print(zone.name, zone.solved)
#             all_solved = False

#     if all_solved == True:
#         print('Congratulations you have won!')
#         time.sleep(10)
#         myPlayer.game_over = True
#         print("do shit")


# win_condition()
# zone['b2'].solved = True
# win_condition()


letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3', '4']
# new = zip(letters, numbers)
new_zones = []
for letter in letters:
    for number in numbers:
        new_zones.append(f"{letter}{number}")

for location in new_zones:
    if location is not "b2":
        zones[location].solved = True