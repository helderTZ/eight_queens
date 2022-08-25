from typing import Tuple, List

def get_diagonal(row: int, col: int) -> List[Tuple[int, int]]:
    positions = []
    r, c = row, col
    while r >= 0 or c >= 0:
        r -= 1
        c -= 1
        positions.append((r, c))
    r, c = row, col
    while r < 8 or c < 8:
        r += 1
        c += 1
        positions.append((r, c))
    r, c = row, col
    while r >= 0 or c < 8:
        r -= 1
        c += 1
        positions.append((r, c))
    r, c = row, col
    while r < 8 or c >= 0:
        r += 1
        c -= 1
        positions.append((r, c))
    return positions


def is_valid(queens: List[Tuple[int, int]], row: int, col: int) -> bool:
    for queen in queens:
        if queen[0] == row or queen[1] == col:
            return False
        if (row, col) in get_diagonal(queen[0], queen[1]):
            return False
    return True


def eight_queens(queens = None):
    if not queens:
        queens = []
    for row in range(len(queens), 8):
        for col in range(8):
            if (row, col) in queens:
                continue
            if is_valid(queens, row, col):
                queens.append((row, col))
                if attempt := eight_queens(queens):
                    return attempt
                else:
                    queens.remove((row, col))
        return False
    return queens


def print_board(queens):
    for row in range(8):
        print('+---+---+---+---+---+---+---+---+\n', end='')
        for col in range(8):
            if col == 0:
                print('|', end='')
            print(' Q |' if (row,col) in queens else '   |', end='')
            if col == 7:
                print('\n', end='')
        if row == 7:
            print('+---+---+---+---+---+---+---+---+\n', end='')


if __name__ == "__main__":
    queens = eight_queens()
    print(queens)
    print_board(queens)