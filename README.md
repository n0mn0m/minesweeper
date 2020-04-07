## About

A simple implementation of Minesweeper using python and the terminal.

Requires Python >= 3.6 for fstrings no other packages required.

May be interesting to others as I used set coordinates to perform the mine
and flag handling instead of nested looping.


```
~/projects/minesweeper$ python3 minesweeper.py

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

Flags placed 0
Total mines 7
Mines left 7
[['x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x']]
```