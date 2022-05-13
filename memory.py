"""
GAME: Memory Game.
AUTHOR 1: Carla Onate Gardella.
AUTHOR 2: Octavio Augusto Aleman Esparza.

DATE: May - 11 - 2022.

"""

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

def selectColors(key): # selectColor function has been added. It returns a specific color depending on the card number.

    if (key >= 0 and key <= 4):
        return 'blue'
    elif (key >= 5 and key <= 8):
        return 'red'
    elif (key >= 9 and key <= 12):
        return 'yellow'
    elif (key >= 13 and key <= 16):
        return 'green'
    elif (key >= 17 and key <= 20):
        return 'purple'
    elif (key >= 21 and key <= 24):
        return 'orange'
    elif (key >= 25 and key <= 28):
        return 'pink'
    elif (key >= 29 and key <= 32):
        return 'black'

    

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

    if mark is not None and hide[mark]: #The function that displays the card number was divided in two parts. Allthough both parts are almost identical, the first one prints a 0 beforehand if the card number is a single digit.
        if tiles[mark] < 10:
            x, y = xy(mark)
            up()
            goto(x + 5, y) #The x coordinate value has been adjusted in order to center the printed numbers.
            color(selectColors(tiles[mark]))
            write('0' + str(tiles[mark]), align="left", font=('Arial', 30, 'normal'))

        elif (tiles[mark] >= 10):
            x, y = xy(mark)
            up()
            goto(x + 5, y) #The x coordinate value has been adjusted in order to center the printed numbers.
            color(selectColors(tiles[mark]))
            write(tiles[mark], align="left", font=('Arial', 30, 'normal'))

    if pairs == 32: # If all the pairs have been discovered
        goto(0, 0)
        color('white') #The color of the winning message will be white and has also been centered.
        write('YOU WON', align="center", font=('Arial', 30, 'normal')) # Write on the center of the screen the game is over
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

