import random


def main():
    name = input("What is your name?\n> ")
    print(f"Hello, {name}!")
    roll(name)


def roll(name):
    print("Rolling dice...")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total value: {total}")
    if total > 7:
        print(f"{name} won!")
    else:
        print(f"{name} lost!")


if __name__ == "__main__":
    main()
