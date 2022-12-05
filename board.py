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


def get_land_layout(map_name: str) -> list:
    """
    Read json file and return a list for "layout" key  for given map_name.

    :param map_name: a string
    :precondition: map_name must be a string, that represents a land name
    :postcondition: reads given file and returns a list for "layout" key for given map_name
    :return: a list

    >>> type(get_land_layout("Verden"))
    <class 'list'>
    >>> get_land_layout("Hogwarts")
    Oops! There is no such land in this version
    """
    with open('maps.json', 'r') as maps_options:
        maps = json.load(maps_options)
    for land_name, layout in maps.items():
        if land_name == map_name:
            return layout["layout"]
        else:
            print("Oops! There is no such land in this version")


def get_map_legend(map_name: str) -> dict:
    """
    Read json file and return a list for "legend" key  for given map_name.

    :param map_name: a string
    :precondition: map_name must be a string, that represents a land name
    :postcondition: reads given file and returns a list for "legend" key for given map_name
    :return: a list

    >>> type(get_map_legend("Verden"))
    <class 'dict'>
    >>> get_map_legend("Hogwarts")
    Oops! There is no such land in this version
    """
    with open('maps.json', 'r') as maps_options:
        maps = json.load(maps_options)
    for land_name, land_info in maps.items():
        if land_name == map_name:
            return land_info["legend"]
        else:
            print("Oops! There is no such land in this version")


def print_map_legend(legend: dict) -> None:
    """
    Print map legend in a table.

    :param legend: a dictionary
    :precondition: legend must be a non-empty dictionary, that contains type of location as a key and
    three characters as a value
    :postcondition: produces a side effect nand prints map legend from given dictionary as a table
    """
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


def make_board(layout: list) -> dict:
    """
    Create dictionary that represents a board

    :param layout: a list
    :precondition: layout must be a non-empty list of lists
    :postcondition: creates a dictionary based on given layout, with tuple as a key and a Location object as a value.
    Creates Location object with column value (location type) from given list.
    :return: a dictionary

    >>> make_board([["Forest"], ["Forest", "Swamp"]])
    {(0, 0): Location("Forest", , None), (1, 0): Location("Forest", , None), (1, 1): Location("Swamp", , None)}
    """
    board = {}
    x_coordinate = 0
    for row in layout:
        y_coordinate = 0
        for location_type in row:
            board[(x_coordinate, y_coordinate)] = Location(location_type)
            y_coordinate += 1
        x_coordinate += 1
    return board


def draw_map(board_typed: dict, legend: dict, current_location: list) -> None:
    """
    Print out board as a table with symbols.

    :param board_typed: a dictionary
    :param legend: a dictionary
    :param current_location: a list
    :precondition: board_typed must be a non-empty dictionary where values are Location objects
    :precondition: legend must be a non-empty dictionary, that contains type of location as a key and
    three characters as a value
    :precondition: current_location must be a non-empty list of integers with length equal to two
    :postcondition: prints out board as a table where each cell contains 3 characters.
    Characters represent location type.
    """
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


def generate_description(board: dict) -> None:
    """
    Generate and set description for each item of given board.

    :param board: a dictionary
    :precondition: board must be a non-empty dictionary where values are Location objects
    :postcondition: checks location_type of Location object,
    generates and sets description out of options provided in descriptions.json for each location_type
    """
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


def add_unique_descriptions(board: dict) -> None:
    """
    Set description for unique locations.

    param board: a dictionary
    :precondition: board must be a non-empty dictionary where values are Location objects
    :postcondition: checks board for locations that match locations in unique_locations_description.json,
    if the match was found, sets the description

    >>> test_board = make_board([["Crossroad"]])
    >>> add_unique_descriptions(test_board)
    >>> description = test_board[(0, 0)].get_description()
    >>> text_one = 'Witcher is outside the tavern on a crossroad. Roadsigns say if you turn to the east, you will reach'
    >>> text_two =' the Verden Mountains. If you fo to the south, you will enter the Royal Forrest, and a Greater Swamp'
    >>> text_three = ' lays to the south-east.'
    >>> text = text_one + text_two + text_three
    >>> text == description
    True
    """
    with open('unique_locations_description.json', 'r') as descriptions_options:
        descriptions = json.load(descriptions_options)
    for location in board.values():
        location_type = location.get_location_type()
        if location_type in descriptions:
            location.set_description(descriptions[location_type])


def activate_enemies(board: dict, enemies: dict) -> None:
    """
    Create and set Enemy objects.

    :param board: a dictionary
    :param enemies: a dictionary
    :precondition: board must be a non-empty dictionary where values are Location objects
    :preconditions: enemies must be a non-empty dictionary
    :postcondition: iterates through each Location on the board, if value of enemy attribute matches enemy name in
    given enemy dictionary, creates and sets Enemy object, and sets its state based on given enemies dictionary

    >>> test_board = make_board([["Forest"]])
    >>> test_board[(0, 0)].set_enemy("Leshy")
    >>> test_enemies = {"enemies" : [{"name" : "Leshy", "description" : "test", "defaultHP" : 20, "experience" : 20 }]}
    >>> activate_enemies(test_board, test_enemies)
    >>> test_board[(0, 0)].get_enemy()
    Enemy(Leshy, 20, 20, test)
    """
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


def set_enemies(board: dict) -> None:
    """
    Set enemy to the board based on enemies.json

    :param board: a dictionary
    :precondition: board must be a non-empty dictionary where values are Location objects
    :postcondition: matches enemies to location type; sets the main monster to the last square of the board;
    invokes enemies creation

    >>> test_board = make_board([["Forest", "Forest"], ["Swamp", "Forest"]])
    >>> set_enemies(test_board)
    >>> test_board[(1, 1)].get_enemy()
    Enemy(Basilisk, 800, 25, The Basilisk)
    """
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
