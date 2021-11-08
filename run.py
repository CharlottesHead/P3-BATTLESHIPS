import random

SHIPS_LENGTH = [2, 3, 3, 4, 5]
PLR_BRD = [[" "] * 8 for i in range(8)]
CPU_BRD = [[" "] * 8 for i in range(8)]
PLR_HIDDEN = [[" "] * 8 for i in range(8)]
CPU_HIDDEN = [[" "] * 8 for i in range(8)]
CONVERT = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    for row_number, row in enumerate(board, start=1):
        print("%d|%s|" % (row_number, "|".join(row)))


# Loop through length of ships and loop until ship fits and doesn't overlap
def place_ships(board):
    for legnth in SHIPS_LENGTH:
        while True:
            if board == CPU_BRD:
                orientation, row, column = random.choice(
                    ["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if (check_fit(legnth, row, column, orientation) and
                    ship_overlaps(board, row, column, orientation,
                                  legnth) is False):
                    if orientation == "H":
                        for i in range(column, column + legnth):
                            board[row][i] = "X"
                    else:
                        for i in range(row, row + legnth):
                            board[i][column] = "X"
                    break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(legnth))
                row, column, orientation = user_input(place_ship)
                if (check_fit(legnth, row, column, orientation) and
                        ship_overlaps(board, row, column, orientation,
                                      legnth) is False):
                    if orientation == "H":
                        for i in range(column, column + legnth):
                            board[row][i] = "X"
                    else:
                        for i in range(row, row + legnth):
                            board[i][column] = "X"
                    print_board(PLR_BRD)
                    break


def check_fit(legnth, row, column, orientation):
    return (orientation != "H" or
            column + legnth <= 8) and (orientation == "H" or row + legnth <= 8)


def ship_overlaps(board, row, column, orientation, legnth):
    if orientation == "H":
        for i in range(column, column + legnth):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + legnth):
            if board[i][column] == "X":
                return True
    return False


def user_input(place_ship):
    if place_ship is True:
        while True:
            try:
                orientation = input(
                    "Enter orientation, H(horizontal) or V(vertical): ").upper(
                )
                if orientation in ["H", "V"]:
                    break
            except TypeError:
                print('Enter a valid orientation H(horizontal) or V(vertical')
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = CONVERT[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = CONVERT[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    if board == PLR_HIDDEN:
        row, column = user_input(PLR_HIDDEN)
        if board[row][column] in ["O", "X"]:
            turn(board)
        elif CPU_BRD[row][column] == "X":
            board[row][column] = "X"
            print("YOU GOT 'EM!! Brilliant work, Admiral.")
        else:
            board[row][column] = "O"
            print("It was probably the wind that blew it off course, Sir.")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] in ["O", "X"]:
            turn(board)
        elif PLR_BRD[row][column] == "X":
            board[row][column] = "X"
            print("Bloody hell! We've been hit!!")
        else:
            board[row][column] = "O"


place_ships(CPU_BRD)
# print_board(CPU_BRD)  # Debugging, remove note to show cpu ships
print_board(PLR_BRD)
place_ships(PLR_BRD)

while True:
    # players turn
    while True:
        print('Select a new target, Admiral')
        print_board(PLR_HIDDEN)
        turn(PLR_HIDDEN)
        break
    if count_hit_ships(PLR_HIDDEN) == 6:
        print("We've won!, Nicely done, Sir. GAME OVER")
        break
    # CPU turn
    while True:
        turn(CPU_HIDDEN)
        break
    print_board(CPU_HIDDEN)
    if count_hit_ships(CPU_HIDDEN) == 6:
        print("Better luck next time, ol' chap.")
        break