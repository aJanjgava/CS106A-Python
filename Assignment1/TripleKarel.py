from karel.stanfordkarel import *


# General function to paint walls.
def main():
    for i in range(3):
        for j in range(2):
            paint_movement()
            another_move()
        paint_movement()
        turn_right()
    turn_left()


# Karel moves and paints wall.
def paint_movement():
    while left_is_blocked():
        put_beeper()
        move()


# Karel keeps going for another walls.
def another_move():
    if left_is_clear():
        turn_left()
        move()


# Karel turns right.
def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
