"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""


from character import Character


def choose_name():
    print('Choose your name for this quest, Witcher.')
    name = input()
    return name


def make_character(name):
    character = Character(name)
    print(f"Welcome to the realm of Thompsons, Monster Hunter {name}. Our lord and soverign, Supereme Ruler")
    print("Christopher, rules with an iron fist.")
    print('Enter anything to continue.')
    input()
    return character


def set_up_character():
    character_name = choose_name()
    return make_character(character_name)
