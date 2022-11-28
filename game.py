"""
Olga Zimina
A01307815
Wilber Lin
A01331142
"""
from board import make_board
from character import make_character, choose_name
from describe import describe_current_location
from control import get_user_choice, validate_move, move_character
from challenge import check_for_challenges, execute_challenge_protocol



def game(): # called from main
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    player_name = choose_name()
    character = make_character(player_name)
    achieved_goal = False
    while not achieved_goal:
        #Tell the user where they are
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenge = check_for_challenges()
            if there_is_a_challenge:
                execute_challenge_protocol(character)
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
