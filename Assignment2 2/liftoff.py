"""
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    for i in range(10, 0, -1):
        print(i)
    print("Blastoff")


if __name__ == "__main__":
    main()
