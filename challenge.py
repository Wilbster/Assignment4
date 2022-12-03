"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import json
import random
import copy


def check_for_challenges(character, enemy_board):
    location = (character.get_current_location()[0], character.get_current_location()[1])
    if enemy_board[location] != ['']:
        return True
    else:
        return False



def execute_challenge_protocol(character, board):

    x_coord = character.get_current_location()[0]
    y_coord = character.get_current_location()[1]
    location = (x_coord, y_coord)

    with open('enemies.json', 'r') as enemies_types:
        enemies = json.load(enemies_types)

    enemy_type = board[location][0]
    hp = 0

    for enemy in enemies['enemies']:
        if enemy['name'] == enemy_type:
            hp = enemy['defaultHP']

    enemy = {'Name': enemy_type, 'HP': hp}

    print(f"You are attacked by a {enemy['Name']}")
    print('Enter anything to continue')
    input()

    print('<-----------------COMBAT HAS BEGUN------------------->')
    while character.get_current_hp() > 0 and enemy['HP'] > 0:
        print(f"You and the {enemy['Name']} lunge at each other.")
        character_roll = (character.get_current_hp())*random.choice((1, 2, 3, 4, 5, 6))
        enemy_roll = enemy['HP']*random.choice((1, 2, 3, 4, 5, 6))
        if character_roll >= enemy_roll:
            print(f"You land a strike on the {enemy['Name']}")
            enemy['HP'] -= 1
            print(f"Your HP: {character.get_current_hp()}")
            print(f"{enemy['Name']}'s HP: {enemy['HP']}")
            print('Enter anything to continue.')
            input()
        else:
            print(f"The {enemy['Name']} lands a strike on you!")
            character.set_current_hp(-1)
            print(f"Your HP: {character.get_current_hp()}")
            print(f"{enemy['Name']}'s HP: {enemy['HP']}")
            print('Enter anything to continue.')
            input()

    if character.get_current_hp() > 0:
        print(f"You have vanquished your foe, {character.get_name()}!")
        print(f"Your renaming HP is, {character.get_current_hp()} out of your max of {character.get_max_hp()}!")
        print('Enter anything to continue.')
        input()
    else:
        print(f"Alas, {character.get_name()}, you have been slain in combat.")


def main():
    pass


if __name__ == '__main__':
    main()
