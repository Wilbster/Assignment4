"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import itertools

from control import get_player_choice


def at_witch_house(character):
    """
    Check whether the charachter is at the 3 Witches Shack.

    :param character: an object of type Character
    :return: a boolean
    """
    if character.get_current_location() == [7, 5]:
        return True
    else:
        return False


def execute_witch_protocol():
    """
    Execute the scenario of the talking frog.
    """

    verse = ['kingchriswantsanitertool']

    print('An enchanted frog appears and starts muttering...')

    verses = itertools.cycle(verse)

    while verses:
        print(f"What sounds like '{next(verses)}'")
        options = ("Let the frog finish.", 'Depart the frog.')
        choice = get_player_choice(options)
        if choice == 'Depart the frog.':
            break


def main():
    """
     Drive the program.
     """


if __name__ == '__main__':
    main()

