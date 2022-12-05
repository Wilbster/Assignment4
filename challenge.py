"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import math
import random

from control import get_player_choice
from magic import execute_combat_magic
from settings import display_narrator_text


def check_for_enemies(character, board):

    x_coord = character.get_current_location()[0]
    y_coord = character.get_current_location()[1]

    location = (x_coord, y_coord)
    enemies_present = board[location].get_enemy()

    if enemies_present is not None:
        print(f"{enemies_present.get_name()} menace you!!! Will you fight or run away?")
        options = ('Fight', 'Hide')
        choice = get_player_choice(options)
        if choice == 'Fight':
            return True
        else:
            return False
    else:
        return False


def execute_combat_protocol(character, board):

    x_coord = character.get_current_location()[0]
    y_coord = character.get_current_location()[1]
    location = (x_coord, y_coord)

    enemy = board[location].get_enemy()
    enemy_name = enemy.get_name()
    experience_to_gain = enemy.get_experience()

    print(f"You fight {enemy_name}")
    print('Enter anything to continue')
    input()

    print('<-----------------COMBAT HAS BEGUN------------------->')
    while character.get_current_hp() > 0 and enemy.get_hp() > 0:
        print(f"You and the {enemy_name} lunge at each other.")
        character_roll = (character.get_current_hp())*random.choice((1, 2, 3, 4, 5, 6))
        enemy_roll = enemy.get_hp() * random.choice((1, 2, 3, 4, 5, 6))
        if character_roll >= enemy_roll:
            print(f"You land a strike on the {enemy_name}")
            enemy.change_hp(-1)
            print(f"Your HP: {character.get_current_hp()}")
            print(f"{enemy_name}'s HP: {enemy.get_hp()}")
        else:
            print(f"The {enemy_name} lands a strike on you!")
            character.change_current_hp(-1)
            print(f"Your HP: {character.get_current_hp()}")
            print(f"{enemy_name}'s HP: {enemy.get_hp()}")
        print('Enter 1 to cast a spell, or enter anything else to continue.')
        choice = input()
        if choice == '1':
            execute_combat_magic(character, enemy)

    if character.get_current_hp() > 0:
        print(f"You have vanquished your foe, {character.get_name()}!")
        print(f"Your renaming HP is, {character.get_current_hp()} out of your max of {character.get_max_hp()}!")
        character.set_experience(experience_to_gain)
        print(f"You have gained {experience_to_gain} experience from this fight. You now have "
              f"{character.get_experience()} points!")
        board[location].set_enemy(None)
        print('Enter anything to continue.')
        input()
    else:
        print(f"Alas, {character.get_name()}, you have been slain in combat.")
        display_narrator_text("game_over_screen.txt")


def is_mission_completed(board: dict) -> bool:
    """
    Define if the main enemy is killed.

    :param board: a dictionary
    :precondition: board must be a non-empty configured dictionary
    :postcondition: evaluates if enemy's hp on th final location is equal to zero
    :return: True - enemy's hp on th final location is equal to zero,
    False - enemy's hp on th final location is greater or less than zero
    """
    max_coordinate = int(math.sqrt(len(board)) - 1)
    return board[(max_coordinate, max_coordinate)].get_enemy() is None


def main():
    """
     Drive the program.
     """


if __name__ == '__main__':
    main()
