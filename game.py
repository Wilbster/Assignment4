"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
from board import get_map_legend, draw_map
from character import Character, character_should_level, level_up
from settings import make_character, display_narrator_text, set_up_board, pause
from describe import describe_current_location
from control import validate_move, get_player_choice
from challenge import check_for_enemies, execute_combat_protocol


def game(): # called from main
    display_narrator_text("start_page.txt")
    pause()
    map_legend = get_map_legend("Verden")
    board = set_up_board("Verden")
    character = make_character()
    achieved_goal = False
    while not achieved_goal and character.get_current_hp() > 0:
        #Tell the user where they are
        situation = "test"
        options = ["North", "South", "West", "East"]
        # describe_current_location(board, character)
        direction = get_player_choice(options)
        valid_move = validate_move(character, direction)
        if valid_move:
            character.move_to(direction)
            print(character.get_current_location())
            character_location = character.get_current_location()
            draw_map(board, map_legend, character_location)
            board[(character_location[0], character_location[1])].describe_location()
            enemy_fight = check_for_enemies(character, board)
            if enemy_fight:
                execute_combat_protocol(character, board)
            if character_should_level(character):
                level_up(character)
            """
                if character_has_leveled():
                    execute_glow_up_protocol()
                achieved_goal = check_if_goal_attained(board, character)
            """

        else:
            print('That is outside the boundaries of our realm!')
            print('Enter anything to continue.')
            input()
            # Tell the user they   can’t go in that direction
    print('<-----GAME OVER----->')


def main():
    game()


if __name__ == '__main__':
    main()
