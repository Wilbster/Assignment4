"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""

from board import get_map_legend, draw_map
from character import character_should_level, level_up
from settings import make_character, display_narrator_text, set_up_board, pause
from control import validate_move, get_player_choice
from challenge import check_for_enemies, execute_combat_protocol, is_mission_completed
from witch import at_witch_house, execute_witch_protocol


def game() -> None:
    """
    Run the game Witcher: Fang of the Devil.
    """

    #display_narrator_text("start_page.txt")
    pause()
    map_legend = get_map_legend("Verden")
    board = set_up_board("Verden")
    character = make_character()
    achieved_goal = False
    while not achieved_goal and character.get_current_hp() > 0:
        # Tell the user where they are
        options = ("North", "South", "West", "East")
        direction = get_player_choice(options)
        valid_move = validate_move(character, direction)
        if valid_move:
            character.move_to(direction)
            print(character.get_current_location())
            character_location = character.get_current_location()
            draw_map(board, map_legend, character_location)
            board[(character_location[0], character_location[1])].describe_location()
            if at_witch_house(character):
                execute_witch_protocol()
            enemy_fight = check_for_enemies(character, board)
            if enemy_fight:
                execute_combat_protocol(character, board)
            if is_mission_completed(board):
                achieved_goal = True
                display_narrator_text("mission_completed_screen.txt")
            if character_should_level(character):
                level_up(character)
        else:
            print('That is outside the boundaries of our realm!')
            print('Enter anything to continue.')
            input()
            # Tell the user they   can’t go in that direction
    print('<-----GAME OVER----->')


def main():
    """
     Drive the program.
     """
    game()


if __name__ == '__main__':
    main()
