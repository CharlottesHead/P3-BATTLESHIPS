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
                    # place ship
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
                    # place ship
                    if orientation == "H":
                        for i in range(column, column + legnth):
                            board[row][i] = "X"
                    else:
                        for i in range(row, row + legnth):
                            board[i][column] = "X"
                    print_board(PLR_BRD)
                    break