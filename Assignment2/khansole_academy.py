import random


def main():
    i = 0
    while i != 3:
        num_one = random.randint(10, 99)
        num_two = random.randint(10, 99)
        total = num_one + num_two
        print(f"What is {num_one} + {num_two}?")

        answer = int(input("Your answer: "))

        if answer == total:
            i = i + 1
            print(f"Correct! You've got {i} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {total}")
            i = 0

        if i == 3:
            print(" Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
