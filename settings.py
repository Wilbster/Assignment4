"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
import time

from character import Character

from board import get_land_layout, make_board, get_map_legend, draw_map, generate_description, set_enemies, \
    add_unique_descriptions


def pause():
    time.sleep(2)


def make_character() -> Character:
    """
    Create character object with given name.

    :postcondition: creates object of Character type with inputed by username
    :return: an object of type Character

    >>> player = Character("Ivan")
    >>> type(player)
    <class 'character.Character'>
    >>> player.get_name()
    'Ivan'
    """
    print('Choose your name for this quest, Witcher.')
    name = input()
    character = Character(name)
    print(f"Welcome to the realm of Thompsons, Monster Hunter {name}. Our lord and soverign, Supereme Ruler")
    print("Christopher, rules with an iron fist.")
    return character


def set_up_board(map_name: str) -> dict:
    """
    Set up board.

    :param map_name: a string
    :precondition: map_name must be a string
    :postcondition: creates board as dictionary and configures it according to provided map name
    :return: a dict
    """
    layout = get_land_layout(map_name)
    board = make_board(layout)
    map_legend = get_map_legend(map_name)
    generate_description(board)
    add_unique_descriptions(board)
    set_enemies(board)
    file_name = f'map_of_{map_name.lower()}.txt'
    display_narrator_text(file_name)
    pause()
    draw_map(board, map_legend, [0, 0])
    pause()
    board[0, 0].describe_location()
    return board


def display_narrator_text(file_name: str) -> None:
    """
    Display content of given file.

    :param file_name: a string
    :preconditions: file_name must be a string, that represents name of existing in the project file
    :postcondition: produces side effect and prints out content of given file
    """
    with open(file_name) as file:
        content = file.readlines()
        for line in content:
            print(line.rstrip())


def main():
    display_narrator_text("start_page.txt")
    display_narrator_text("game_over_screen.txt")
    display_narrator_text("mission_completed_screen.txt")


if __name__ == '__main__':
    main()
