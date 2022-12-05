"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import itertools

from control import get_player_choice


def at_witch_house(character):
    if character.get_current_location() == [7, 5]:
        return True
    else:
        return False


def execute_witch_protocol():

    verse = ['kingchriswantsanitertool']

    print('An enchanted frog appears and starts muttering...')

    verses = itertools.cycle(verse)

    while object:
        print(f"What sounds like '{next(verses)}'")
        options = ("Let the frog finish.", 'Depart the frog.')
        choice = get_player_choice(options)
        if choice == 'Depart the frog.':
            break


def main():
    execute_witch_protocol()


if __name__ == '__main__':
    main()

