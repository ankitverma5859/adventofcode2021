
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
    for boardnumber in range(0, num_of_boards):
        for row in range(0, 5):
            for col in range(0, 5):
                if boards[boardnumber][row][col] == num:
                    boards[boardnumber][row][col] = 'X'


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


def check_winner():
    global boards, num_of_boards
    for board_number in range(0, num_of_boards):
        for row in range(0, 5):
            if check_row(board_number, row):
                return board_number
        for col in range(0, 5):
            if check_column(board_number, col):
                return board_number
    return -1


def play_bingo():
    for itr, num in enumerate(draw_order):
        mark_num_in_boards(num)
        draw_order[itr] = 'X'
        if itr >= 5:
            board_number = check_winner()
            print()
            if board_number != -1:
                show_boards()
                show_draw_order()
                print(f'Answer:{sum_unmarked_number(board_number)*int(num)}')
                break


read_data()
prepare_draw_order()
prepare_bingo_boards()
play_bingo()
