"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""


def get_user_choice():

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
        return get_user_choice()


def validate_move(board, character, direction):
    coordinates = (character['X-coordinate'], character['Y-coordinate'])
    if direction == 'North':
        new_coord = coordinates[1] - 1
        new_coordinates = (coordinates[0], new_coord)
    elif direction == 'South':
        new_coord = coordinates[1] + 1
        new_coordinates = (coordinates[0], new_coord)
    elif direction == 'West':
        new_coord = coordinates[0] - 1
        new_coordinates = (new_coord, coordinates[1])
    elif direction == 'East':
        new_coord = coordinates[0] + 1
        new_coordinates = (new_coord, coordinates[1])
    if new_coordinates in board:
        return True
    else:
        return False

def move_character(character, direction):
    if direction == 'North':
        character['Y-coordinate'] -= 1
    elif direction == 'South':
        character['Y-coordinate'] += 1
    elif direction == 'West':
        character['X-coordinate'] -= 1
    elif direction == 'East':
        character['X-coordinate'] += 1

def main():
    pass


if __name__ == '__main__':
    main()