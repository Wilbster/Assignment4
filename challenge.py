"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import random
import copy


def check_for_challenges():
    return random.choice((True, False))


def execute_challenge_protocol(character):
    drunk_bandit = {'Name': 'Band of drunk bandits', 'HP': 3}

    enemy = copy.deepcopy(drunk_bandit)

    print(f"You are attacked by a {enemy['Name']}")
    print('Enter anything to continue')
    input()

    print('<-----------------COMBAT HAS BEGUN------------------->')
    while character['Current HP'] > 0 and enemy['HP'] > 0:
        print(f"You and the {enemy['Name']} lunge at each other.")
        character_roll = (character['Max HP']**2)*random.choice((1, 2, 3, 4, 5, 6))
        enemy_roll = enemy['HP']*random.choice((1, 2, 3, 4, 5, 6))
        if character_roll >= enemy_roll:
            print(f"You land a strike on the {enemy['Name']}")
            enemy['HP'] -= 1
            print(f"Your HP: {character['Current HP']}")
            print(f"{enemy['Name']}'s HP: {enemy['HP']}")
            print('Enter anything to continue.')
            input()
        else:
            print(f"The {enemy['Name']} lands a strike on you!")
            character['Current HP'] -= 1
            print(f"Your HP: {character['Current HP']}")
            print(f"{enemy['Name']}'s HP: {enemy['HP']}")
            print('Enter anything to continue.')
            input()

    if character['Current HP'] > 0:
        print(f"You have vanquished your foe, {character['Name']}!")
        print(f"Your renaming HP is, {character['Current HP']} out of your max of {character['Max HP']}!")
        print('Enter anything to continue.')
        input()
    else:
        print(f"Alas, {character['Name']}, you have been slain in combat.")


def main():
    pass


if __name__ == '__main__':
    main()
