"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_depper()
    Karel_goes_home()

def double_depper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()

def turn_around():
    for i in range(2):
        turn_left()

def Karel_goes_home():
    turn_around()
    if not front_is_clear():
        turn_around()
    else:
        move()
        turn_around()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
