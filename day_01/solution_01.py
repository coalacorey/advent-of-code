def main():
    input = open('input.txt', 'r')
    lines = input.readlines()
    lines_copy = lines.copy()
    solve_part_1(lines)
    solve_part_2(lines_copy)


def solve_part_1(lines):
    max = 0
    temp = 0
    for line in lines:
        if len(line.strip()) == 0:
            if temp > max:
                max = temp
            temp = 0
        else:
            temp += int(line)
    print("Part 1: " + str(max))


def solve_part_2(lines):
    totals = list()
    temp = 0
    for line in lines:
        if len(line.strip()) == 0:
            totals.append(temp)
            temp = 0
        else:
            temp += int(line)
    totals.append(temp)
    totals.sort(reverse=True)
    print("Part 2: " + str(sum(totals[0:3])))


if __name__ == '__main__':
    main()
