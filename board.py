"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

import json
import math
import random

from prettytable import PrettyTable

from enemy import Enemy

from location import Location


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
    table = PrettyTable(headers[:(2 * len(headers)//3)])
    table.add_row(symbols[:(2 * len(symbols)//3)])
    print(table)
    table = PrettyTable(headers[(2 * len(headers) // 3):])
    table.add_row(symbols[(2 * len(symbols) // 3):])
    print(table)


def make_board(layout):
    board = {}
    x_coordinate = 0
    for row in layout:
        y_coordinate = 0
        for location_type in row:
            board[(x_coordinate, y_coordinate)] = Location(location_type)
            y_coordinate += 1
        x_coordinate += 1
    return board


def draw_map(board_typed, legend, current_location):
    rows = set()
    columns = set()
    for key in board_typed.keys():
        rows.add(key[0])
        columns.add(key[1])
    for row in rows:
        for column in columns:
            # get location type assigned for (row, column)
            location_type = board_typed[(row, column)].get_location_type()
            if current_location == [row, column]:
                # if character's location is equal to (row, column), print X
                print(f"| X | ", end="")
            else:
                print(f"|{legend[location_type]}| ", end="")
        print()
    print_map_legend(legend)


def generate_description(board):
    with open('descriptions.json', 'r') as descriptions_options:
        descriptions = json.load(descriptions_options)
    for location in board.values():
        location_type = location.get_location_type()
        if location_type in descriptions:
            type_description_options = descriptions[location_type]
            location_description_type = random.choices(type_description_options["type"])
            location_description_surroundings = random.choices(type_description_options["surrounding"])
            location_description_sounds = random.choices(type_description_options["sounds"])
            location.set_description(' '.join(location_description_type + location_description_surroundings +
                                              location_description_sounds))


def add_unique_descriptions(board):
    with open('unique_locations_description.json', 'r') as descriptions_options:
        descriptions = json.load(descriptions_options)
    for location in board.values():
        location_type = location.get_location_type()
        if location_type in descriptions:
            location.set_description(descriptions[location_type])


def activate_enemies(board, enemies):
    for location in board.values():
        enemy_name = location.get_enemy()
        if enemy_name:
            alive_enemy = Enemy(enemy_name)
            location.set_enemy(alive_enemy)
            for enemy in enemies["enemies"]:
                if enemy["name"] == enemy_name:
                    enemy_data = enemy
                    alive_enemy.set_description(enemy_data["description"])
                    alive_enemy.set_hp(enemy_data["defaultHP"])
                    alive_enemy.set_experience(enemy_data["experience"])
                    break


def set_enemies(board):
    with open('enemies.json', 'r') as enemies_types:
        enemies = json.load(enemies_types)
    enemies_per_type_location = {}
    for enemy in enemies["enemies"]:
        if enemy["location"] not in enemies_per_type_location:
            enemies_per_type_location[enemy["location"]] = [enemy["name"]]
        else:
            enemies_per_type_location[enemy["location"]].append(enemy["name"])
    for location in board.values():
        location_type = location.get_location_type()
        if location_type in enemies_per_type_location.keys():
            location.set_enemy((random.choices(enemies_per_type_location[location_type] + ['']))[0])
    max_coordinate = int(math.sqrt(len(board)) - 1)
    board[(max_coordinate, max_coordinate)].set_enemy('Basilisk')
    activate_enemies(board, enemies)


def main():
    """
     Drive the program.
     """


if __name__ == '__main__':
    main()
