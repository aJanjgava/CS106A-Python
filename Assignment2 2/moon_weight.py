MOON_WEIGHT = 16.5 / 100


def main():
    weight_on_earth = float(input("Enter your weight: "))
    if weight_on_earth > 0:
        weight_on_moon = weight_on_earth * MOON_WEIGHT
        print(f"Your weight on the moon is {weight_on_moon}")
    else:
        print("Sorry, you can't have a negative weight")


if __name__ == '__main__':
    main()
