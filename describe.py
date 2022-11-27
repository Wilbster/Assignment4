"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import math


def describe_current_location(board, character):

    name = character['Name']
    dictionary_length = len(board)
    board_side_length = int(math.sqrt(dictionary_length))
    coordinates = (character['X-coordinate'], character['Y-coordinate'])
    location_description = board[coordinates]

    game_map = ''
    for y_coordinate in range(board_side_length):
        for x_coordinate in range(board_side_length):
            if (x_coordinate, y_coordinate) == coordinates:
                game_map += '#&'
            else:
                if location_description == 'Empty Room':
                    game_map += '[]'
        game_map += '\n'
    print(game_map)

    print(f'{name}, you have encountered an {location_description}.')



def main():
    pass


if __name__ == '__main__':
    main()