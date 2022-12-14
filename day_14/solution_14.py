#!/usr/bin/env python3


# For animation purposes 
# import time


def main():
    print("--- Day 14: Regolith Reservoir ---")
    input = tuple(open('input.txt', 'r').readlines())
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    sand = (500, 0)
    stones = generate_stone_coordinates(input)
    y_max = max([(s[1], s[0]) for s in stones])[0]
    cave_map = generate_cave_map(stones, y_max)
    res = spawn_sand(cave_map, y_max, sand)
    return res


def solve_part_2(input):
    sand = (500, 0)
    stones = generate_stone_coordinates(input)
    y_max = max([(s[1], s[0]) for s in stones])[0] + 2
    cave_map = generate_cave_map(stones, y_max)
    res = spawn_sand_2(cave_map, y_max, sand)
    return res


def generate_stone_coordinates(input):
    stones = set()
    for line in input:
        points = line.strip().split("->")
        for index in range(len(points) - 1):
            if index < len(points) - 1:
                s_1 = points[index].strip().split(",")
                s_2 = points[index + 1].strip().split(",")
                point_1 = (int(s_1[0]), int(s_1[1]))
                point_2 = (int(s_2[0]), int(s_2[1]))
                stones.add((point_1[0], point_1[1]))
                stones.add((point_2[0], point_2[1]))
                # y-coordinate different
                if point_1[0] == point_2[0]:
                    s = sorted([point_1, point_2], key=lambda x: x[1])
                    for y in range(s[0][1], s[1][1]):
                        stones.add((point_1[0], y))
                # x-coordinate different
                if point_1[1] == point_2[1]:
                    s = sorted([point_1, point_2], key=lambda x: x[0])
                    for x in range(s[0][0], s[1][0]):
                        stones.add((x, point_1[1]))
    return stones


def generate_cave_map(stones, y_max):
    x_min = min(stones)[0]
    x_max = max(stones)[0]
    map = dict()
    for y in range(0, y_max + 1):
        for x in range(x_min, x_max + 1):
            # stone = 1, air = 0
            map[(x, y)] = int((x, y) in stones)
    return map


def get_printable_cave_map(cave_map, y_max):
    x_min = min(cave_map.keys())[0]
    x_max = max(cave_map.keys())[0]
    output = ""
    for y in range(0, y_max + 1):
        row = []
        for x in range(x_min, x_max + 1):
            if y == y_max:
                row.append("#")
            else:
                if cave_map.get((x, y), 0) == 1:
                    row.append("#")
                elif cave_map.get((x, y), 0) == 0:
                    row.append(".")
                elif cave_map.get((x, y), 0) == 2:
                    row.append("o")
        output += "".join(row) + "\n"
    return output


def spawn_sand(cave_map, y_max, sand_position):
    rest = 0
    x_min = min(cave_map.keys())[0]
    x_max = max(cave_map.keys())[0]
    new_position = sand_position
    while new_position != (-1, -1):
        # time.sleep(0.01)
        # print(get_printable_cave_map(cave_map, y_max), end='\r')
        old_position = new_position
        new_position = possible_fall_position(cave_map, old_position)
        if new_position != (-1, -1):
            if new_position[0] >= x_min and new_position[0] <= x_max and new_position[1] <= y_max:
                cave_map[old_position] = 0
                cave_map[new_position] = 2
            else:
                return rest
        else:
            rest += 1
            if cave_map[old_position] == 0:
                new_position = old_position
            else:
                new_position = sand_position


def spawn_sand_2(cave_map, y_max, sand_position):
    rest = 0
    x_min = min(cave_map.keys())[0]
    x_max = max(cave_map.keys())[0]
    new_position = sand_position
    while new_position != (-1, -1):
        # time.sleep(0.01)
        # print(get_printable_cave_map(cave_map, y_max), end='\r')
        old_position = new_position
        new_position = possible_fall_position(cave_map, old_position)
        if old_position == sand_position and new_position == (-1, -1):
            cave_map[old_position] = 2
            return rest + 1
        if new_position != (-1, -1):
            if new_position[0] < x_min and new_position[1] < y_max:
                x_min = new_position[0]
                # append map column
                for y in range(0, y_max):
                    cave_map[x_min, y] = 0
                cave_map[x_min, y_max] = 1
            elif new_position[0] > x_max and new_position[1] < y_max:
                x_max = new_position[0]
                # append map column
                for y in range(0, y_max):
                    cave_map[x_max, y] = 0
                cave_map[x_max, y_max] = 1

            if new_position[1] == y_max:
                cave_map[old_position] = 2
                cave_map[(new_position[0], new_position[1])] = 1
                new_position = old_position
        else:
            cave_map[old_position] = 2
            new_position = sand_position
            rest += 1


def possible_fall_position(map, sand_position):
    # check below
    if map.get((sand_position[0], sand_position[1] + 1), 0) == 0:
        return (sand_position[0], sand_position[1] + 1)
    # check below left
    elif map.get((sand_position[0] - 1, sand_position[1] + 1), 0) == 0:
        return (sand_position[0] - 1, sand_position[1] + 1)
    # check below right
    elif map.get((sand_position[0] + 1, sand_position[1] + 1), 0) == 0:
        return (sand_position[0] + 1, sand_position[1] + 1)
    # no position to fall to
    return (-1, -1)


if __name__ == '__main__':
    main()
