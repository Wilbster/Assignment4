"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

import json

from prettytable import PrettyTable


map_art = """___  ___                     __   _   _              _            
|  \/  |                    / _| | | | |            | |           
| .  . | __ _ _ __     ___ | |_  | | | | ___ _ __ __| | ___ _ __  
| |\/| |/ _` | '_ \   / _ \|  _| | | | |/ _ \ '__/ _` |/ _ \ '_ \ 
| |  | | (_| | |_) | | (_) | |   \ \_/ /  __/ | | (_| |  __/ | | |
\_|  |_/\__,_| .__/   \___/|_|    \___/ \___|_|  \__,_|\___|_| |_|
             | |                                                  
             |_|        """


def get_land_layout(map_name):
    with open('maps.json', 'r') as maps_options:
        maps = json.load(maps_options)
    for land_name, layout in maps.items():
        if land_name == map_name:
            return layout["layout"]
        else:
            print("Oops! There is no such land in this version")


def get_map_legend(map_name):
    with open('maps.json', 'r') as maps_options:
        maps = json.load(maps_options)
    for land_name, land_info in maps.items():
        if land_name == map_name:
            return land_info["legend"]
        else:
            print("Oops! There is no such land in this version")


def print_map_legend(legend):
    print()
    print('MAP LEGEND')
    headers = ["You are here"]
    symbols = ["X"]
    for location_type, symbol in legend.items():
        headers.append(location_type)
        symbols.append(symbol)
    table = PrettyTable(headers)
    table.add_row(symbols)
    print(table)


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
    print(f'{map_art}\n')
    rows = set()
    columns = set()
    for key in board_typed.keys():
        rows.add(key[0])
        columns.add(key[1])
    for row in rows:
        for column in columns:
            location_type = board_typed[(row, column)]  # get location type assigned for (row, column)
            if current_location == [row, column]:
                print(f"| X | ", end="")  # if character's location is equal to (row, column), print X
            else:
                print(f"|{legend[location_type]}| ", end="")
        print()
    print_map_legend(legend)



def main():
    layout = get_land_layout("Verden")
    board = make_board(layout)
    map_legend = get_map_legend("Verden")
    print('legend:', map_legend)
    draw_map(board, map_legend, [0, 0])

    # pass


if __name__ == '__main__':
    main()
