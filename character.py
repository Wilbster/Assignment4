"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""


def make_character(name):
    character = {"Name": name, "Level": 1, "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Max HP": 5,
                 "Experience": 0}
    return character


def choose_name():

    print('Choose you name for this quest:')
    name = input()
    return name


def main():
    pass


if __name__ == '__main__':
    main()
