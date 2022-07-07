from karel.stanfordkarel import *


# Karel have fun with checkerboard.
def main():
    odd_lane_paint()
    turn_back()
    while left_is_clear():
        move_another_lane()
        even_lane_paint()
        turn_back()
        if left_is_clear():
            move_another_lane()
            odd_lane_paint()
            turn_back()


# Karel paints odd lanes.
def odd_lane_paint():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


# Karel paints eve lanes.
def even_lane_paint():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


# Karel moves another lane.
def move_another_lane():
    turn_left()
    move()
    turn_right()


# Karel turns back after work.
def turn_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()


# Right!
def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
