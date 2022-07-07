from karel.stanfordkarel import *


def main():
    # Code for Karel movement, Main code.
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_back()
    move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()
    turn_back()


def turn_right():
    # Code to move Karel right side.
    for i in range(3):
        turn_left()


def turn_back():
    # Turn Karel back.
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
