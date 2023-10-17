import math


def main():
    print("--- Day 11: Monkey in the Middle ---")
    print("Solution part 1: " + str(solve_part_1()))
    print("Solution part 2: " + str(solve_part_2()))


def solve_part_1():
    monkey_inspections = [0, 0, 0, 0, 0, 0, 0, 0]
    monkey_modulos = [11, 5, 19, 13, 7, 17, 2, 3]
    monkey_partners = [[2, 3], [4,0], [5,6], [2,6], [0,3], [7,1], [7,5], [4,1]]
    monkeys = get_monkeys()
    for _ in range(0, 20):
        for monkey in range(8):
            while len(monkeys[monkey]) > 0:
                monkey_inspections[monkey] = monkey_inspections[monkey] + 1
                wl = get_worry_level_after_inspection(
                    monkeys[monkey].pop(0), monkey)
                wl = int(math.floor(wl/3))
                if wl % monkey_modulos[monkey] == 0:
                    receiving_monkey = monkey_partners[monkey][0]
                else:
                    receiving_monkey = monkey_partners[monkey][1]
                monkeys[receiving_monkey].append(wl)
    monkey_inspections.sort(reverse=True)
    return monkey_inspections[0] * monkey_inspections[1]


def solve_part_2():
    monkey_inspections = [0, 0, 0, 0, 0, 0, 0, 0]
    monkey_modulos = [11, 5, 19, 13, 7, 17, 2, 3]
    monkey_partners = [[2, 3], [4,0], [5,6], [2,6], [0,3], [7,1], [7,5], [4,1]]
    monkeys = get_monkeys()
    lcm = math.lcm(11, 5, 19, 13, 7, 17, 2, 3)
    for _ in range(0, 10000):
        for monkey in range(8):
            while len(monkeys[monkey]) > 0:
                monkey_inspections[monkey] = monkey_inspections[monkey] + 1
                level = monkeys[monkey].pop(0)
                wl = get_worry_level_after_inspection(level, monkey)
                if wl % monkey_modulos[monkey] == 0:
                    receiving_monkey = monkey_partners[monkey][0]
                else:
                    receiving_monkey = monkey_partners[monkey][1]
                monkeys[receiving_monkey].append(wl % lcm)
    monkey_inspections.sort(reverse=True)
    return monkey_inspections[0] * monkey_inspections[1]


def get_worry_level_after_inspection(old, monkey):
    new = 0
    if monkey == 0:
        new = old * 5
    elif monkey == 1:
        new = old * 11
    elif monkey == 2:
        new = old + 2
    elif monkey == 3:
        new = old + 5
    elif monkey == 4:
        new = old * old
    elif monkey == 5:
        new = old + 4
    elif monkey == 6:
        new = old + 6
    elif monkey == 7:
        new = old + 7
    return new


def get_monkeys():
    monkeys = {}
    monkeys[0] = [83, 88, 96, 79, 86, 88, 70]
    monkeys[1] = [59, 63, 98, 85, 68, 72]
    monkeys[2] = [90, 79, 97, 52, 90, 94, 71, 70]
    monkeys[3] = [97, 55, 62]
    monkeys[4] = [74, 54, 94, 76]
    monkeys[5] = [58]
    monkeys[6] = [66, 63]
    monkeys[7] = [56, 56, 90, 96, 68]
    return monkeys


if __name__ == '__main__':
    main()
