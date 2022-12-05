import copy


def main():
    print("--- Day 5: Supply Stacks ---")
    lines = open('input.txt', 'r').readlines()
    stacks = extract_stacks(lines)
    moves = extract_moves(lines)
    print("Solution part 1: " + str(solve_part_1(copy.deepcopy(stacks), moves)))
    print("Solution part 2: " + str(solve_part_2(copy.deepcopy(stacks), moves)))


def solve_part_1(stacks, moves):
    res = ""
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2] - 1].append(stacks[move[1] - 1].pop())
    for stack in stacks:
        res = res + stack.pop()
    return res


def solve_part_2(stacks, moves):
    res = ""
    for move in moves:
        temp = []
        for _ in range(move[0]):
            temp.append(stacks[move[1] - 1].pop())
        stacks[move[2] - 1] = stacks[move[2] - 1] + list(reversed(temp))
    for stack in stacks:
        res = res + stack.pop()
    return res


def extract_stacks(lines):
    stacks = []
    for stack in range(9):
        pos = 1 + (4 * stack)
        temp = []
        for item in range(8):
            if lines[item][pos].isalpha():
                temp.append(lines[item][pos])
        stacks.append(list(reversed(temp)))
    return stacks


def extract_moves(lines):
    moves = lines[lines.index('\n') + 1:]
    temp = []
    for move in moves:
        m = [int(n) for n in move.split() if n.isdigit()]
        temp.append(m)
    return temp


if __name__ == '__main__':
    main()
