#!/usr/bin/env python3


import functools


AMOUNT_ROCKS_1 = 2022
AMOUNT_ROCKS_2 = 1000000000000
CAVE_WIDTH = 7
CAVE_BOUNDS = (-1, 7)
ROCK_SHAPES = [
    ((2, 0), (3, 0), (4, 0), (5, 0)),  # ----
    ((3, 0), (2, 1), (3, 1), (4, 1), (3, 2)),  # +
    ((2, 0), (3, 0), (4, 0), (4, 1), (4, 2)),  # reverse L
    ((2, 0), (2, 1), (2, 2), (2, 3)),  # I
    ((2, 0), (3, 0), (2, 1), (3, 1))]  # Square

past = {}


def main():
    print("--- Day 17: Pyroclastic Flow ---")
    input = tuple(open('input.txt', 'r').readlines())
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    return (simulate(input, AMOUNT_ROCKS_1))


def solve_part_2(input):
    return (simulate_2(input, AMOUNT_ROCKS_2))


def simulate(input, amount):
    push_pattern = get_push_pattern(input)
    blocked_blocks = {0: [[0, 0], [1, 0], [
        2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]}

    # Save blocked blocks and delete them once a row get's filled completely
    position = 0
    # highest_block = 0
    # lowest_row_in_blocked_blocks = 0
    for rock in range(amount):
        # print(rock + 1)
        # print(position)
        # if there is no row in blocked blocks for the current row, add an empty list
        # rock_pattern = push_pattern[rock % len(push_pattern)]
        highest = sorted(blocked_blocks.keys())[-1]
        fall_height = highest + 4
        blocked_blocks, position = simulate_rock_fall(ROCK_SHAPES[rock % len(
            ROCK_SHAPES)], push_pattern, position, fall_height, blocked_blocks)

        # Code for keeping the indexes as small as possible when blocks get reset, has a bug
        # lowest_row_in_blocked_blocks = sorted(blocked_blocks.keys())[0]
        # if lowest_row_in_blocked_blocks > 0:
        #     add = sorted(blocked_blocks.keys())[-1]
        # print("Adding " + str(add))
        # highest_block =  highest_block + add
        # print(lowest_row_in_blocked_blocks)
        # print(blocked_blocks)
        # new_blocked_blocks = {}
        # for key in blocked_blocks.keys():
        #     for value in blocked_blocks[key]:
        #         new_blocked_blocks[(key - lowest_row_in_blocked_blocks)] = new_blocked_blocks.get((key - lowest_row_in_blocked_blocks), []) + [[value[0], value[1] - lowest_row_in_blocked_blocks]]
        # new_blocked_blocks[(key - lowest_row_in_blocked_blocks)] = list(sorted(new_blocked_blocks[(key - lowest_row_in_blocked_blocks)], key=lambda x: x[0]))
        # print(new_blocked_blocks)
        # blocked_blocks = new_blocked_blocks
        # highest_block = highest_block - sorted(blocked_blocks.keys())[-1]
    # highest_block += sorted(blocked_blocks.keys())[-1]
    # print(sorted(blocked_blocks.keys()))
    # return highest_block
    return sorted(blocked_blocks.keys())[-1]


# Currently reddit solution hybrid, need to implement a new cycle detection algo
def simulate_2(input, amount):
    push_pattern = get_push_pattern(input)
    blocked_blocks = {0: [[0, 0], [1, 0], [
        2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]}

    position = 0
    i = 0
    height = 0
    while not (answer := check_past(i, position, height, AMOUNT_ROCKS_2)):
        highest = sorted(blocked_blocks.keys())[-1]
        fall_height = highest + 4
        blocked_blocks, position = simulate_rock_fall(ROCK_SHAPES[i % len(
            ROCK_SHAPES)], push_pattern, position, fall_height, blocked_blocks)
        height = sorted(blocked_blocks.keys())[-1]
        i += 1
    return (answer)


def check_past(i, position, height, amount):
    key = (i % len(ROCK_SHAPES), position)
    if key in past:
        old_i, old_height = past[key]
        if (int(amount) - i) % (i - old_i) == 0:
            return (height +
                    int(amount - i) // (i - old_i) * (height - old_height))
    else:
        past[key] = (i, height)


def get_push_pattern(input):
    pattern = []
    for line in input:
        line = line.strip()
        for c in line:
            if c == ">":
                pattern.append(1)
            elif c == "<":
                pattern.append(-1)
    # print(len(pattern))
    return pattern


def simulate_rock_fall(rock_shape, rock_pattern, position, fall_height, blocked_blocks):
    rock = spawn_rock(rock_shape, fall_height)
    while True:
        rock = move_rock_sideways(
            rock, rock_pattern[position % len(rock_pattern)], blocked_blocks)
        position = (position + 1) % len(rock_pattern)
        new_rock = move_rock_down(rock, blocked_blocks)
        # If we can move down we do, otherwise we update the new highest blocks
        if rock != new_rock:
            rock = new_rock
        else:
            return update_blocked_blocks(blocked_blocks, rock), position


@functools.lru_cache(maxsize=None)
def spawn_rock(rock_shape, fall_height):
    rock = []
    for sq in rock_shape:
        rock.append([sq[0], sq[1] + fall_height])
    return rock


def move_rock_sideways(rock, direction, blocked_blocks):
    # Right
    if direction == 1:
        rock_boundary = sorted(rock, key=lambda x: x[0])[-1]
        # If we are at 6 we'd move out of bounds by moving right
        if rock_boundary[0] + direction >= CAVE_BOUNDS[1]:
            return rock
        for sq in rock:
            moved_sq = [sq[0] + direction, sq[1]]
            if moved_sq in blocked_blocks.get(moved_sq[1], []):
                return rock
        new_rock = []
        for sq in rock:
            new_rock.append([sq[0] + direction, sq[1]])
        return new_rock
    # Left
    elif direction == -1:
        rock_boundary = sorted(rock, key=lambda x: x[0])[0]
        # If we are at 0 we'd move out of bounds by moving left
        if rock_boundary[0] + direction <= CAVE_BOUNDS[0]:
            return rock
        for sq in rock:
            moved_sq = [sq[0] + direction, sq[1]]
            if moved_sq in blocked_blocks.get(moved_sq[1], []):
                return rock
        new_rock = []
        for sq in rock:
            new_rock.append([sq[0] + direction, sq[1]])
        return new_rock
    raise NotImplementedError


def move_rock_down(rock, blocked_blocks):
    new_rock = []
    for sq in rock:
        new_sq = [sq[0], sq[1] - 1]
        # If by moving down we hit one of the highest block, we can't move down and have to update highest blocks to include the new rock
        if new_sq in blocked_blocks.get(new_sq[1], []):
            return rock
        # Otherwise we can move downwards
        else:
            new_rock.append(new_sq)
    return new_rock


def update_blocked_blocks(blocked_blocks, rock):
    # Appends rocks into the correct row
    for key in set([r[1] for r in rock]):
        rocks = [ro for ro in rock if ro[1] == key]
        blocked_blocks[key] = blocked_blocks.get(key, []) + rocks

    highest_blocked_row_index = -1
    # We search for the highest row that's completely filled and remove everything below as it is unreachable
    for key in blocked_blocks.keys():
        if len(blocked_blocks[key]) == CAVE_WIDTH:
            highest_blocked_row_index = key

    if highest_blocked_row_index == -1:
        return blocked_blocks
    else:
        new_dictionary = dict(blocked_blocks)
        for key in blocked_blocks.keys():
            if key != highest_blocked_row_index:
                del new_dictionary[key]
            else:
                return new_dictionary
        return blocked_blocks


if __name__ == '__main__':
    main()
