"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
from board import make_board, get_land_layout, get_map_legend, draw_map
from character import Character
from settings import make_character, choose_name
from describe import describe_current_location
from control import validate_move, get_player_choice
from challenge import check_for_challenges, execute_challenge_protocol



def game(): # called from main
    layout = get_land_layout("Verden")
    board = make_board(layout)
    map_legend = get_map_legend("Verden")
    character = Character("OZ")
    draw_map(board, map_legend, character.get_current_location())
    achieved_goal = False
    while not achieved_goal:
        #Tell the user where they are
        situation = "test"
        options = ["North", "South", "West", "South"]
        # describe_current_location(board, character)
        direction = get_player_choice(situation, options)
        valid_move = validate_move(character, direction)
        if valid_move:
            character.move_to(direction)
            # move_character(character, direction)
            print(character.get_current_location())
            character_location = character.get_current_location()
            draw_map(board, map_legend, character_location)
            # describe_current_location(board, character)
            # there_is_a_challenge = check_for_challenges()
            # if there_is_a_challenge:
            #     execute_challenge_protocol(character)
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
    # Print end of game stuff like congratulations or sorry you died


def main():
    game()


if __name__ == '__main__':
    main()
