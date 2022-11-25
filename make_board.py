"""
Wilber Lin
A01331142
"""


def make_board(rows, columns):
    """
    Return a board with the given number of rows and columns.

    :param rows: an int
    :param columns: an int
    :precondition: rows and columns must be integers
    :postcondition: a board with the given number of rows and columns is returned
    :return: a dictionary board
    """
    board = {}

    for i in range(rows):
        for j in range(columns):
            board[(i, j)] = 'Empty Room'

    return board




def main():
    pass


if __name__ == '__main__':
    main()
