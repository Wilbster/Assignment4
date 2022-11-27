"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""


def make_character(name):
    character = {"Name": name, "Level": 1, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Max HP": 5,
                 "Experience": 0}
    print(f"Welcome to the realm of Thompsons, Monster Hunter {name}. Our lord and soverign, Supereme Ruler")
    print("Christopher, rules with an iron fist.")
    print('Enter anything to continue.')
    input()
    return character


def choose_name():

    print('Choose your name for this quest, Witcher.')
    name = input()
    return name


def main():
    pass


if __name__ == '__main__':
    main()
