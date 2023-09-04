import random
import sys
 
def print_grid(player_position):
    for row in range(5):
        for col in range(5):
            if (row, col) == player_position:
                print('P', end=' ')
            else:
                print('_', end=' ')
        print()
 
def move_player(player_position, direction):
    row, col = player_position
    if direction == 'N' and row > 0:
        return row - 1, col
    elif direction == 'S' and row < 4:
        return row + 1, col
    elif direction == 'E' and col < 4:
        return row, col + 1
    elif direction == 'W' and col > 0:
        return row, col - 1
    else:
        input("Out of bounds!")
        sys.stdout.write("\033[F") 
        sys.stdout.write("\033[K")
        return player_position
 
def clear_previous_lines():
    sys.stdout.write("\033[F")  # Move cursor up one line
    sys.stdout.write("\033[K")  # Clear line
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F") 
    sys.stdout.write("\033[K")
    sys.stdout.flush()
 
def main():
    player_position = (random.randint(0, 4), random.randint(0, 4))
 
    print("Welcome to the 5x5 Grid Game!")
    print("Enter 'N', 'S', 'E', or 'W' to move. Enter 'Q' to quit.")
    
    while True:
        clear_previous_lines()  # Clear previous 6 lines
        print_grid(player_position)
        direction = input("Enter your move: ").upper()
        
        if direction == 'Q':
            print("Thanks for playing!")
            break
        
        if direction in ['N', 'S', 'E', 'W']:
            player_position = move_player(player_position, direction)
        else:
            print("Invalid input. Enter 'N', 'S', 'E', 'W', or 'Q'.")
 
if __name__ == "__main__":
    main()