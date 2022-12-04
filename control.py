"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import copy

from exceptions import OutOfTheRealmError


def get_player_choice_v1():

    print('Choose a direction in which to explore.')
    print('1: North --- 2: South --- 3: East --- 4: West')
    choice = input()
    if choice == '1':
        return 'North'
    elif choice == '2':
        return 'South'
    elif choice == '3':
        return 'East'
    elif choice == '4':
        return 'West'
    else:
        print('Invalid')
        return get_player_choice_v1()


def show_available_options(options):
    for number, option in enumerate(options, 1):
        print(f'{number} - {option}')


def get_player_choice(options):
    for option in enumerate(options, 1):
        print(f"{option[0]}: {option[1]}")
    choice = input("Enter your choice ")
    while choice not in '1234':
        print("You must be tired from your long journeys. Take another shot")
        choice = input("Enter your choice ")
    choice = int(choice)
    for number, option in enumerate(options, 1):
        if choice == number:
            print(f"You have selected {option}")
            return option


def define_updated_location(character, direction):
    current_location = copy.copy(character.get_current_location())
    if direction == 'North':
        current_location[0] -= 1
    elif direction == 'South':
        current_location[0] += 1
    elif direction == 'West':
        current_location[1] -= 1
    elif direction == 'East':
        current_location[1] += 1
        print('updated location', current_location)
        print('user location:', character.get_current_location)
    return current_location


def validate_move(character, direction):
    updated_location = define_updated_location(character, direction)
    if updated_location[0] < 0 or updated_location[1] < 0 or updated_location[0] > 9 or updated_location[1] > 9:
        # raise OutOfTheRealmError()
        print("You have reached the world's edge. None but dragons play past here. You should turn back.")
        return False
    else:
        return True


def main():
    pass


if __name__ == '__main__':
    main()
