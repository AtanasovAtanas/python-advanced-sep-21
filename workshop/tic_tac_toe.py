from errors import InvalidPositionError


def read_first_player_sign(first_player_name):
    while True:
        first_player_sign = input(f'{first_player_name} would you like to play with X or O? ').upper()
        if first_player_sign in ['X', 'O']:
            return first_player_sign


def read_players_info():
    first_player_name = input('Player one name: ')
    second_player_name = input('Player two name: ')

    first_player_sign = read_first_player_sign(first_player_name)
    second_player_sign = 'O' if first_player_sign == 'X' else 'X'
    return [first_player_name, first_player_sign], [second_player_name, second_player_sign]


def print_board_numeration():
    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')


def get_coords_by_pos(position):
    if position == 1:
        return 0, 0
    if position == 2:
        return 0, 1
    if position == 3:
        return 0, 2
    if position == 4:
        return 1, 0
    if position == 5:
        return 1, 1
    if position == 6:
        return 1, 2
    if position == 7:
        return 2, 0
    if position == 8:
        return 2, 1
    if position == 9:
        return 2, 2
    raise InvalidPositionError(f'{position} is invalid position. Please provide a valid position in range [1-9]!')


def display_board(matrix):
    for row in matrix:
        print('|  ', end='')
        print('  |  '.join(row), end='')
        print('  |')


def is_board_full(matrix):
    for row in matrix:
        is_row_full = all([el != ' ' for el in row])
        if not is_row_full:
            return False
    return True


def has_player_won(matrix, player_sign):
    # horizontal
    for row in matrix:
        if all([el == player_sign for el in row]):
            return True

    # vertical
    size = len(matrix)
    for col in range(size):
        won = True
        for row in range(size):
            if matrix[row][col] != player_sign:
                won = False
                break
        if won:
            return True

    # primary diagonal
    won = True
    for idx in range(size):
        if matrix[idx][idx] != player_sign:
            won = False
            break
    if won:
        return True

    # secondary diagonal
    won = True
    for idx in range(size):
        if matrix[idx][size - 1 - idx] != player_sign:
            won = False
            break
    return won


def play(matrix, p1, p2):
    turns = 1
    # p1: 1, 3, 5, 7, 9... +2
    # p2: 2, 4, 6, 8, 19... +2
    players_turns = {0: p2, 1: p1}
    while True:
        name, sign = players_turns[turns % 2]

        try:
            position = int(input(f'{name} choose a free position [1-9]: '))
            row, col = get_coords_by_pos(position)

            if matrix[row][col] != ' ':
                raise InvalidPositionError(f'{position} is already taken! Please choose a free position!')

            matrix[row][col] = sign
            turns += 1

            display_board(matrix)

            if has_player_won(matrix, sign):
                print(f'{name} has won!')
                break

            if is_board_full(matrix):
                print('draw!')
                break
        except ValueError:
            print('Please provide a valid position in range [1-9]!')
        except InvalidPositionError as error:
            print(error)


player1, player2 = read_players_info()

print_board_numeration()

print(f'{player1[0]} starts first!')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

play(board, player1, player2)
