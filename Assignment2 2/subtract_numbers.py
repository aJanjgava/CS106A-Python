"""
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from another")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 - num2
    print(f"The result is {total}")


if __name__ == '__main__':
    main()
