def main():
    print("--- Day 5: Supply Stacks ---")
    datastream = open('input.txt', 'r').readlines()[0]
    print("Solution part 1: " + str(solve_part_1(datastream)))
    print("Solution part 2: " + str(solve_part_2(datastream)))


def solve_part_1(datastream):
    for i in range(0, len(datastream) - 5):
        if len([True for n in range(0,3) if datastream[i + n] not in datastream[i+n+1:i+4]]) == 3:
            return i + 4


def solve_part_2(datastream):
    for i in range(0, len(datastream) - 15):
        if len([True for n in range(0,13) if datastream[i + n] not in datastream[i+n+1:i+14]]) == 13:
            return i + 14


if __name__ == '__main__':
    main()
