"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

import json


map_art = """___  ___                     __   _   _              _            
|  \/  |                    / _| | | | |            | |           
| .  . | __ _ _ __     ___ | |_  | | | | ___ _ __ __| | ___ _ __  
| |\/| |/ _` | '_ \   / _ \|  _| | | | |/ _ \ '__/ _` |/ _ \ '_ \ 
| |  | | (_| | |_) | | (_) | |   \ \_/ /  __/ | | (_| |  __/ | | |
\_|  |_/\__,_| .__/   \___/|_|    \___/ \___|_|  \__,_|\___|_| |_|
             | |                                                  
             |_|        """


map_legend = {"Tavern": ("TVN", "unique"),
              "Cowshed": ("CSD", "unique"),
              "Stable": ("SBL", "unique"),
              "Grass field": ("⚘⚘⚘", "basic"),
              "Mountains": ("ꤺꤺꥃ", "basic"),
              "River": ("~~~", "basic"),
              "Swamp": ("_-_", "basic"),
              "Forest": ("///", "basic"),
              "Scorched earth": ("...", "basic"),
              "Forester's shack": ("SHK", "unique"),
              "3 Witches house": ("3WH", "unique"),
              "Mountain troll cave": ("TCV", "unique"),
              "Crossroad": ("CRD", "unique"),
              "Basilisk cave": ("BCV", "unique")}


def print_map_legend(legend):
    print()
    print('MAP LEGEND')
    print(' X  - you are here')
    for location_type in legend:
        print(f' {legend[location_type][0]} - {location_type}')


def get_land_layout(map_name):
    with open('maps.json', 'r') as maps_options:
        maps = json.load(maps_options)
    for land_name, layout in maps.items():
        if land_name == map_name:
            return layout
        else:
            print("Oops! There is no such land in this version")
    print(maps)


def make_board(layout):
    board = {}
    x_coordinate = 0
    for row in layout:
        y_coordinate = 0
        for column in row:
            board[(x_coordinate, y_coordinate)] = column
            y_coordinate += 1
        x_coordinate += 1
    return board


def draw_map(board_typed, legend, current_location):
    print(map_art)
    rows = set()
    columns = set()
    for key in board_typed.keys():
        rows.add(key[0])
        columns.add(key[1])
    for row in rows:
        for column in columns:
            location_type = board_typed[(row, column)]  # get location type assigned for (row, column)
            if current_location == (row, column):
                print(f"| X | ", end="")  # if character's location is equal to (row, column), print X
            else:
                print(f"|{legend[location_type][0]}| ", end="")
        print()
    print_map_legend(legend)


def main():
    layout = get_land_layout("Verden")
    board = make_board(layout)
    draw_map(board, map_legend, (1, 1))
    # pass


if __name__ == '__main__':
    main()
