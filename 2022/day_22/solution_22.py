#!/usr/bin/env python3

move_map = {"L": -90, "R": 90}
dir_map = {0: "U", 90: "R", 180: "D", 270: "L"}
res_map = {0: 3, 90: 0, 180: 1, 270: 2}
# Initially facing to the right
INITIAL_DIRECTION = 90


def main():
    print("--- Day X ---")
    input = tuple(open('input.txt', 'r').readlines())
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    board, moves = parse_input(input)
    start_pos = get_row(0, board)[0]
    player = tuple([start_pos, INITIAL_DIRECTION])
    visit(player, board)
    while moves:
        move = moves.pop(0)
        if move.isalpha():
            player = rotate(player, move_map[move])
            visit(player, board)
        else:
            for _ in range(int(move)):
                visitable, tile = tile_visitable(player, board)
                if visitable:
                    player = (tile, player[1])
                    visit(player, board)
    return 1000 * (player[0][1] + 1) + 4 * (player[0][0] + 1) + res_map[player[1]]


def solve_part_2(input):
    return 0


def parse_input(input: tuple):
    blank_index = input.index("\n")
    board = build_board(input[:blank_index])
    moves = build_moves(input[blank_index+1:][0])
    return board, moves


def build_board(input: tuple):
    board = dict()
    for y, row in enumerate(input):
        for x, item in enumerate(row):
            if item == ".":
                board[tuple([x, y])] = ""
            elif item == "#":
                board[tuple([x, y])] = "S"
            else:
                continue
    return board


def build_moves(input: tuple):
    input = input.strip()
    moves = list()
    digit = ""
    for m in input:
        if m.isalpha():
            if digit != "":
                moves.append(digit)
                digit = ""
            moves.append(m)
        else:
            digit = digit + m
    if digit != "":
                moves.append(digit)
    return moves


def get_row(row, board: dict):
    return [r for r in board.keys() if r[1] == row]


def get_column(col, board: dict):
    return [c for c in board.keys() if c[0] == col]


def get_stones(positions: list, board: dict):
    return [n for n in positions if board[n] == "S"]


def visit(player, board):
    board[player[0]] = dir_map[player[1]]


def rotate(player, rotation):
    return (player[0], (player[1] + rotation) % 360)
    


def tile_visitable(player, board):
    if player[1] == 0:
        col = get_column(player[0][0], board)
        player_index = col.index(player[0])
        new_index = player_index - 1
        if new_index < 0:
            new_index = len(col) + new_index
        to_visit = col[new_index % len(col)]
        if board[to_visit] == "S":
            return False, to_visit
        else:
            return True, to_visit
    elif player[1] == 90:
        row = get_row(player[0][1], board)
        player_index = row.index(player[0])
        new_index = player_index + 1
        if new_index < 0:
            new_index = len(row) + new_index
        to_visit = row[new_index % len(row)]
        if board[to_visit] == "S":
            return False, to_visit
        else:
            return True, to_visit
    elif player[1] == 180:
        col = get_column(player[0][0], board)
        player_index = col.index(player[0])
        new_index = player_index + 1
        if new_index < 0:
            new_index = len(col) + new_index
        to_visit = col[new_index % len(col)]
        if board[to_visit] == "S":
            return False, to_visit
        else:
            return True, to_visit
    elif player[1] == 270:
        row = get_row(player[0][1], board)
        player_index = row.index(player[0])
        new_index = player_index - 1
        if new_index < 0:
            new_index = len(row) + new_index
        to_visit = row[new_index % len(row)]
        if board[to_visit] == "S":
            return False, to_visit
        else:
            return True, to_visit


if __name__ == '__main__':
    main()
