horses_sign = [" X", "* "]
signs = [" X", "* ", "__"]

def print_board():
    print('-' * (column * 3 + 3))

    for i in range(rows, 0, -1):
        print(i, end='| ')
        print(' '.join(board[i - 1]) + ' |')
    print('-' * (column * 3 + 3))
    print("  ", end="")
    for j in range(1, column + 1):
        print(f"{j}".rjust(3), end="")


def knights_move(a, b):
    board[b - 1][a - 1] = ' X'


def next_move(a, b):
    moves = 1
    knights_move(a, b)
    check_moves(a, b, column, rows)
    count_moves(a, b, column, rows)
    print_board()
    while True:
        moves += 1
        ksp = input("\nEnter your next move: ").split()

        try:
            a = int(ksp[0])
            b = int(ksp[1])
        except (ValueError, IndexError):
            print("Invalid dimensions!")
        else:
            if a > column or b > rows:
                print("Invalid move!")
            elif a < 1 or b < 1:
                print("Invalid move!")
            elif len(ksp) != 2:
                print("Invalid move!")
            elif board[b - 1][a - 1] in signs:
                print("Invalid move!")
            elif board[b - 1][a - 1] not in signs:
                for i in range(column):
                    for j in range(rows):
                        if board[j][i] == " X":
                            board[j][i] = "* "
                        if board[j][i] != "* ":
                            board[j][i] = "__"
                knights_move(a, b)
                check_moves(a, b, column, rows)
                posmov = 0
                for i in range(column):
                    for j in range(rows):
                        if board[j][i] == " O":
                            posmov += 1
                if posmov == 0:
                    if moves == rozmiar:
                        print("What a great tour! Congratulations!")
                        break
                    else:
                        print_board()
                        print("\nNo more possible moves!")
                        print(f"Your knight visited {moves} squares!")
                        break
                count_moves(a, b, column, rows)
                print_board()


def check_moves(a, b, column, rows):
    if (b - 2) > 0 and (a - 1) > 0 and board[b - 3][a - 2] not in horses_sign:
        board[b - 3][a - 2] = ' O'
    if (b - 2) > 0 and a + 1 <= column and board[b - 3][a] not in horses_sign:
        board[b - 3][a] = ' O'
    if (b + 2) <= rows and (a - 1) > 0 and board[b + 1][a - 2] not in horses_sign:
        board[b + 1][a - 2] = ' O'
    if (b + 2) <= rows and a + 1 <= column and board[b + 1][a] not in horses_sign:
        board[b + 1][a] = ' O'
    if (a - 2) > 0 and (b - 1) > 0 and board[b - 2][a - 3] not in horses_sign:
        board[b - 2][a - 3] = ' O'
    if (a - 2) > 0 and b + 1 <= rows and board[b][a - 3] not in horses_sign:
        board[b][a - 3] = ' O'
    if (a + 2) <= column and (b - 1) > 0 and board[b - 2][a + 1] not in horses_sign:
        board[b - 2][a + 1] = ' O'
    if (a + 2) <= column and b + 1 <= rows and board[b][a + 1] not in horses_sign:
        board[b][a + 1] = ' O'


def count_moves(a, b, column, rows):
    for i in range(column):
        for j in range(rows):
            if board[j][i] == " O":
                a = i + 1
                b = j + 1

                count = 0
                if (b - 2) > 0 and (a - 1) > 0 and board[b - 3][a - 2] not in horses_sign:
                    count += 1
                if (b - 2) > 0 and (a + 1) <= column and board[b - 3][a] not in horses_sign:
                    count += 1
                if (b + 2) <= rows and (a - 1) > 0 and board[b + 1][a - 2] not in horses_sign:
                    count += 1
                if (b + 2) <= rows and a + 1 <= column and board[b + 1][a] not in horses_sign:
                    count += 1
                if (a - 2) > 0 and (b - 1) > 0 and board[b - 2][a - 3] not in horses_sign:
                    count += 1
                if (a - 2) > 0 and b + 1 <= rows and board[b][a - 3] not in horses_sign:
                    count += 1
                if (a + 2) <= column and (b - 1) > 0 and board[b - 2][a + 1] not in horses_sign:
                    count += 1
                if (a + 2) <= column and b + 1 <= rows and board[b][a + 1] not in horses_sign:
                    count += 1

                board[b - 1][a - 1] = f' {count}'


while True:
    board_dim = input("Enter your board dimensions: ").split()

    try:
        column = int(board_dim[0])
        rows = int(board_dim[1])
    except (ValueError, IndexError):
        print("Invalid dimensions!")
    else:
        if column < 1 or rows < 1:
            print("Invalid dimensions!")
        elif len(board_dim) != 2:
            print("Invalid dimensions!")
        else:
            rozmiar = column * rows
            break


while True:
    ksp = input("Enter the knight's starting position: ").split()

    try:
        a = int(ksp[0])
        b = int(ksp[1])
    except (ValueError, IndexError):
        print("Invalid dimensions!")
    else:
        if a > column or b > rows:
            print("Invalid dimensions!")
        elif a < 1 or b < 1:
            print("Invalid dimensions!")
        elif len(ksp) != 2:
            print("Invalid dimensions!")
        else:
            break

board = [['__' for i in range(column)] for j in range(rows)]
#knights_move(a, b)
#check_moves(a, b, column, rows)
#count_moves(a, b, column, rows)
#print_board()
next_move(a, b)
