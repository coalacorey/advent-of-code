import math


def main():
    print("--- Day 9: Rope Bridge ---")
    datastream = open('input.txt', 'r').readlines()
    print("Solution part 1: " + str(solve_generic_for_n_knots(datastream, 1)))
    print("Solution part 2: " + str(solve_generic_for_n_knots(datastream, 9)))


def solve_generic_for_n_knots(datastream, rope_length):
    initial_position = [0, 0]
    rope = []
    for _ in range(rope_length + 1):
        rope.append([initial_position])
    for line in datastream:
        line = line.split()
        move = line[0]
        steps = int(line[1])
        for _ in range(steps):
            update_head(rope[0], move)
            for knot in range(1, rope_length + 1):
                update_knot(rope[knot], rope[knot - 1][-1])
    res = set()
    for position in rope[-1]:
        res.add(tuple(position))
    return len(res)


def update_head(head, move):
    current_position = head[-1]
    new_position = [current_position[0], current_position[1]]
    if move == "U":
        new_position[1] = new_position[1] + 1
    if move == "D":
        new_position[1] = new_position[1] - 1
    if move == "L":
        new_position[0] = new_position[0] - 1
    if move == "R":
        new_position[0] = new_position[0] + 1
    head.append(new_position)


def update_knot(knot, head_position):
    current_position = knot[-1]
    new_position = [current_position[0], current_position[1]]
    difference = [head_position[0] - current_position[0],
                  head_position[1] - current_position[1]]
    # If we are on the head or diagonal from the head but still connect we don't move at all
    if (abs(difference[0]) == 0 and abs(difference[1] == 0)):
        return
    if (abs(difference[0]) == 1 and abs(difference[1]) == 1):
        return
    # if x and y parameter are different and not null the head is positioned diagonally from the tail
    if (abs(difference[0]) == 2 and difference[1] != 0) or (abs(difference[1]) == 2 and difference[0] != 0):
        # If the difference is (+-)2, that means the head moved in that direction
        # Positive means right or up, negative means left or down
        if difference[0] == 2:
            new_position[0] = new_position[0] + 1
            new_position[1] = new_position[1] + int(math.copysign(1, difference[1]))
            knot.append(new_position)
            return
        if difference[0] == -2:
            new_position[0] = new_position[0] - 1
            new_position[1] = new_position[1] + int(math.copysign(1, difference[1]))
            knot.append(new_position)
            return
        if difference[1] == 2:
            new_position[0] = new_position[0] + int(math.copysign(1, difference[0]))
            new_position[1] = new_position[1] + 1
            knot.append(new_position)
            return
        if difference[1] == -2:
            new_position[0] = new_position[0] + int(math.copysign(1, difference[0]))
            new_position[1] = new_position[1] - 1
            knot.append(new_position)
            return
    elif (abs(difference[0]) == 2 and difference[1] == 0) or (abs(difference[1]) == 2 and difference[0] == 0):
        # If the y difference is positive, that means the head moved up, tail follows up
        if difference[1] == 2:
            new_position[1] = new_position[1] + 1
            knot.append(new_position)
            return
        # If the y difference is negative, that means the head moved down, tail follows down
        if difference[1] == -2:
            new_position[1] = new_position[1] - 1
            knot.append(new_position)
            return
        # If the x difference is positive, that means the head moved right, tail follows right
        if difference[0] == 2:
            new_position[0] = new_position[0] + 1
            knot.append(new_position)
            return
        # If the y difference is negative, that means the head moved down, tail follows down
        if difference[0] == -2:
            new_position[0] = new_position[0] - 1
            knot.append(new_position)
            return


if __name__ == '__main__':
    main()
