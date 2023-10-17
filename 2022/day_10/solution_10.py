def main():
    print("--- Day 10: Cathode-Ray Tube ---")
    datastream = open('input.txt', 'r').readlines()
    print("Solution part 1: " + str(solve_part_1(datastream)))
    print("Solution part 2: " + str(solve_part_2(datastream)))


def solve_part_1(datastream):
    sum = 0
    checkpoints = [20, 60, 100, 140, 180, 220]
    cycle = 0
    x = 1
    for line in datastream:
        line = line.replace("\n", "")
        if line == 'noop':
            cycle += 1
            if cycle in checkpoints:
                sum += (cycle * x)
        else:
            for _ in range(0, 2):
                cycle += 1
                if cycle in checkpoints:
                    sum += (cycle * x)
            x += int(line.split()[1])
    return sum


def solve_part_2(datastream):
    screen = []
    for _ in range(6):
        line = []
        for _ in range(40):
            line.append(".")
        screen.append(line)
    cycle = 0
    x = 1
    for line in datastream:
        line = line.replace("\n", "")
        if line == 'noop':
            cycle += 1
            l = int(cycle / 40)
            p = (cycle % 40) - 1
            if p in range(x-1, x + 2):
                screen[l][p] = "#"
        else:
            for _ in range(0, 2):
                cycle += 1
                l = int(cycle / 40)
                p = (cycle % 40) - 1
                if p in range(x-1, x + 2):
                    screen[l][p] = "#"
            x += int(line.split()[1])
    for l in screen:
        print(" ".join(l))
    return 0


if __name__ == '__main__':
    main()
