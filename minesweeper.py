"""
Mine Sweeper

Input coordinates in xyc format where:

x = the position on the x axis
y = the position on the y axis
c = the command type. f for flag c for clear

Rules:
There are a set number of mines on the board.
Mark them all with a flag (f) while not attempting
to clear any coordinates that contain a mine.

Each time you clear an empty tile that tile will
show you how many mines are neighboring that tile.

To remove a placed flag enter the coordinates of
the tile with a flag and the flag command (eg. 23f)
and the flag will be removed.

Enter 'help' at any time to see this screen again.
"""

import itertools
import random
import sys
from pprint import pprint as pp


def setup_gameboard(grid_size, mine_ratio=.2):
    grid = [["x"] * grid_size for i in range(grid_size) ]
    mine_count = int(grid_size * grid_size * .2)
    # We don't have to actually put the moves on the board.
    # The board is nothing but a set of coordinates that we
    # are tracking the state of. Since the mines are relatively
    # Sparse we can have then in a set, and do set operations
    # against the mines instead of have to loop a matrix over
    # and over.
    mine_coords = set()

    # This could in theory be infinite by really really
    # bad luck, but doubtful
    while len(mine_coords) < mine_count:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)

        mine = f"{x}{y}"

        if mine not in mine_coords: 
            mine_coords.add(mine)

    return grid, mine_coords

def set_flag(grid, flags, move):
    coord = move[:2]
    x = int(coord[0])
    y = int(coord[1])
    if coord in flags:
        flags.remove(coord)
        grid[x][y] = "x"
    else:
        flags.add(coord)
        grid[x][y] = "f"

    return grid

def clear_tile(grid, mines, move):
    """
    Clear the tile, and display how many neighboring tiles are mines. If the cleared
    tile is a mine see if they user wants to play again.
    """
    coord = move[:2]
    pp(coord)
    if coord in mines:
        print("BOOM! You hit a mine.")
        again = input("\nPlay again (y/n)? ")
        if again == "y":
            play_game()
        else:
            sys.exit()
    else:
        x = int(coord[0])
        y = int(coord[1])
        # Neighbors in rows above and below, we are not checking indices in
        # the grid otherwise you would need to guard these.
        neighbors = 0
        row_neighbords = (x-1, x, x+1)
        column_neighbords = (y-1, y, y+1)
        possible_mines = itertools.product(row_neighbords, column_neighbords)
        for neighbor in possible_mines:
            possible_mine = f"{neighbor[0]}{neighbor[1]}"
            if possible_mine in mines:
                neighbors += 1
        grid[x][y] = f"{neighbors}"
        return grid

def play_game():
    """
    Top level function that initializes game variables
    and puts us into the user input eval loop.
    """
    grid_size = 6
    grid, mines = setup_gameboard(grid_size)
    mine_count = len(mines)
    flag_count = 0
    flags = set()
    # Uncomment to make testing easier.
    # print(f"DEBUG: {mines}\n\n")
    
    while flags != mines:
        print(f"Flags placed {len(flags)}")
        print(f"Total mines {len(mines)}")
        print(f"Mines left {len(mines - flags)}")
        pp(grid)

        move = input(f"\nCoordinate (xy from 0 to {grid_size -1} and command: ")

        if move == "exit":
            sys.exit()
        elif len(move) != 3 or move == "help":
            print(__doc__)
        elif move[2] == "f":
            try:
                grid = set_flag(grid, flags, move)
            except IndexError:
                print(f"Invalid coordinates. Coordinates should be between 0 and {grid_size-1}")
        elif move[2] == "c":
            try:
                grid = clear_tile(grid, mines, move)
            except IndexError:
                print(f"Invalid coordinates. Coordinates should be between 0 and {grid_size-1}")
        else:
            print("Unknown command type.\n\nPlease enter coord (xy) follow by f or c (flag or clear).\n\nEnter 'help' for more information.\n\n")

    print("\n\nCongratulations you've found all the mines!")
    pp(mines)
    pp(grid)

    again = input("\n\nPlay again (y/n)? ")
    if again == "y":
        play_game()
    else:
        sys.exit()


if __name__ == "__main__":
    print(__doc__)
    play_game()

