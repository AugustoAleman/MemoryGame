"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

# Carla Oñate Gardella A01653555

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0
pairs = 0 # variable to count number of pairs discovered

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps, pairs
    taps += 1 # Sum each tap on the screen
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        pairs += 1 # If the user found a pair add it to the total
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    if pairs == 32: # If all the pairs have been discovered
        goto(0, 0)
        write('YOU WON', font=('Arial', 30, 'normal')) # Write on the center of the screen the game is over
        return

    up()
    goto(-200, 220) # go to the top left corner of the screen
    tapsString = 'Taps: ' + str(taps) # The string to be shown
    write(tapsString, font=('Arial', 10, 'normal')) # Write tap amount on the screen
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 440, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
