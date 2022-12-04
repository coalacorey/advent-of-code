def main():
    print("--- Day 4: Camp Cleanup ---")
    input = open('input.txt', 'r')
    lines = input.readlines()
    print("Solution part 1: " + str(solve_part_1(lines)))
    print("Solution part 2: " + str(solve_part_2(lines)))


def solve_part_1(lines):
    res = 0
    for line in lines:
        one = set(range(int(line.split(',')[0].split(
            '-')[0]), int(line.split(',')[0].split('-')[1]) + 1))
        two = set(range(int(line.split(',')[1].split(
            '-')[0]), int(line.split(',')[1].split('-')[1]) + 1))
        if one <= two or two <= one:
            res += 1
    return res


def solve_part_2(lines):
    res = 0
    for line in lines:
        one = set(range(int(line.split(',')[0].split(
            '-')[0]), int(line.split(',')[0].split('-')[1]) + 1))
        two = set(range(int(line.split(',')[1].split(
            '-')[0]), int(line.split(',')[1].split('-')[1]) + 1))
        if one & two:
            res += 1
    return res


if __name__ == '__main__':
    main()
