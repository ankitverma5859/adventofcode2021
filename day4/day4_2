
data = ""
draw_order = []
boards = []
num_of_boards = 0
filename = "data.txt"


def read_data():
    global data, filename
    file = open(filename, "r+")
    data = file.read().split('\n')


def prepare_draw_order():
    global data, draw_order
    draw_order = data[0].split(',')


def prepare_bingo_boards():
    global data, boards, num_of_boards
    board_numbers = []

    for itr in range(2, len(data)):
        numbers = data[itr].split(' ')
        for num in numbers:
            if num != '':
                board_numbers.append(num)

    num_of_boards = int(len(board_numbers) / 25)
    board = []
    board_row = []
    for itr, board_number in enumerate(board_numbers):
        board_row.append(board_number)
        if itr != 0 and (itr + 1) % 5 == 0:
            board.append(board_row)
            board_row = []
        if itr != 0 and (itr + 1) % 25 == 0:
            boards.append(board)
            board = []


def show_boards():
    global boards, num_of_boards
    for board_number in range(0, num_of_boards):
        for row in range(0, 5):
            for col in range(0, 5):
                    print(boards[board_number][row][col], end=" ")
            print(' ')
        print('\n')


def show_draw_order():
    global draw_order
    print(draw_order)


def sum_unmarked_number(board_number):
    global boards, draw_order
    sum_of_unmarked_number = 0
    for row in range(0, 5):
        for col in range(0, 5):
            if boards[board_number][row][col] != 'X':
                sum_of_unmarked_number = sum_of_unmarked_number + int(boards[board_number][row][col])
    return sum_of_unmarked_number


def mark_num_in_boards(num):
    global boards, num_of_boards
    for board_number in range(0, num_of_boards):
        for row in range(0, 5):
            for col in range(0, 5):
                if boards[board_number][row][col] == num:
                    boards[board_number][row][col] = 'X'


def check_column(board_number, col_number):
    x_count = 0
    for itr in range(0, 5):
        if boards[board_number][itr][col_number] == 'X':
            x_count = x_count + 1
    if x_count == 5:
        return 1
    else:
        return 0


def check_row(board_number, row_number):
    x_count = 0
    for itr in range(0, 5):
        if boards[board_number][row_number][itr] == 'X':
            x_count = x_count + 1
    if x_count == 5:
        return 1
    else:
        return 0


def check_winner(remaining_boards):
    global boards, num_of_boards
    winner_indexes = []
    for board_index, board_number in enumerate(remaining_boards):
        if board_number != 'X':
            for row in range(0, 5):
                if check_row(board_number, row):
                    winner_indexes.append(board_index)
            for col in range(0, 5):
                if check_column(board_number, col):
                    winner_indexes.append(board_index)
    return winner_indexes


def number_of_remaining_boards(remaining_boards):
    count = 0
    for board in remaining_boards:
        if board != 'X':
            count = count + 1
    return count


def play_bingo():
    global num_of_boards
    remaining_boards = list(range(0, num_of_boards))
    for itr, num in enumerate(draw_order):
        mark_num_in_boards(num)
        draw_order[itr] = 'X'

        if itr >= 5:
            board_indexes = check_winner(remaining_boards)

            if board_indexes:
                if number_of_remaining_boards(remaining_boards) > 1:
                    for board_index in board_indexes:
                        remaining_boards[board_index] = 'X'
                else:
                    print(f'Answer:{sum_unmarked_number(remaining_boards[board_indexes[0]]) * int(num)}')
                    break


read_data()
prepare_draw_order()
prepare_bingo_boards()
play_bingo()
