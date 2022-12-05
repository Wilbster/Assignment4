"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import copy
import sys

from character import Character


def get_player_choice(options: list) -> tuple:
    """
    Get player choice.

    :param options: a list
    :precondition: options must bbe a non-empty list
    :postcondition: checks if player input matches number of any provided option,
    if match is found - returns tuple(number, option); else ask user for input.
    If player enters 'quit', the programm will be stoped
    :return: tuple of int and string
    """
    for option in enumerate(options, 1):
        print(f"{option[0]}: {option[1]}")
    choice = input("Enter your choice ")
    if choice == "quit":
        sys.exit("This is it for today. Rest well!")
    while choice not in str([digit+1 for digit in range(len(options))]):
        print("You must be tired from your long journeys. Take another shot")
        choice = input("Enter your choice ")
    choice = int(choice)
    for number, option in enumerate(options, 1):
        if choice == number:
            print(f"You have selected {option}")
            return option


def define_updated_location(character: Character, direction: str) -> list:
    """
    Calculate location based on given direction

    :param character: a Character object
    :param direction: a string
    :precondition: character must be aCharacter object
    :precondition: direction must be one of the following strings:
    "North", "South", "East", "West"
    :postcondition: calculates current location based on given direction
    :return: a list

    >>> witcher = Character("Gerall")
    >>> define_updated_location(witcher, "South")
    [1, 0]
    """
    current_location = copy.copy(character.get_current_location())
    if direction == 'North':
        current_location[0] -= 1
    elif direction == 'South':
        current_location[0] += 1
    elif direction == 'West':
        current_location[1] -= 1
    elif direction == 'East':
        current_location[1] += 1
    return current_location


def validate_move(character: Character, direction: str) -> bool:
    """
    Validate player move

    :param character: a Character object
    :param direction: a string
    :precondition: character must be aCharacter object
    :precondition: direction must be one of the following strings:
    "North", "South", "East", "West"
    :postcondition: validates player move and returns False if any element of new location is less than zero or
    greater than 9, else True
    :return: False - if any element of new location is less than zero or greater than 9, else True
    """
    updated_location = define_updated_location(character, direction)
    if updated_location[0] < 0 or updated_location[1] < 0 or updated_location[0] > 9 or updated_location[1] > 9:
        print("You have reached the world's edge. None but dragons play past here. You should turn back.")
        return False
    else:
        return True


def main():
    """
     Drive the program.
     """


if __name__ == '__main__':
    main()
