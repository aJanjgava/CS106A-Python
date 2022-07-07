from karel.stanfordkarel import *


# Main function for Karel to repair the walls.
def main():
    while front_is_clear():
        wall_repair()
        return_bottom()
        move_forward()
    if front_is_blocked():
        wall_repair()
        return_bottom()


# Karel turns right.
def turn_right():
    for i in range(3):
        turn_left()


# Karel moves forward.
def forward_move():
    if front_is_clear():
        for i in range(4):
            move()


# Karel returns to starting point.
def starting_point():
    while right_is_clear():
        turn_right()
        move()
        turn_left()


# Karel repairs walls.
def wall_repair():
    while left_is_clear():
        if beepers_present():
            turn_left()
            move()
            turn_right()
        else:
            put_beeper()
            turn_left()
            move()
            turn_right()
    if no_beepers_present():
        put_beeper()


# Karel returns bottom.
def return_bottom():
    while right_is_clear():
        turn_right()
        move()
        turn_left()


# Karel goes for next!
def move_forward():
    for i in range(4):
        move()


if __name__ == "__main__":
    run_karel_program()
