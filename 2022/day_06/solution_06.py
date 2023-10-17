def main():
    print("--- Day 6: Tuning Trouble ---")
    datastream = open('input.txt', 'r').readlines()[0]
    print("Solution part 1: " + str(solve_part_1(datastream)))
    print("Solution part 2: " + str(solve_part_2(datastream)))


def solve_part_1(datastream):
    return find_index_of_n_distinct_characters(datastream, 4)


def solve_part_2(datastream):
    return find_index_of_n_distinct_characters(datastream, 14)


def find_index_of_n_distinct_characters(datastream, n):
    offset = 0
    for i in range(0, len(datastream) - (n + 1)):
        i = i + offset
        offset = 0
        found = 1
        for k in range(0, n - 1):
            if datastream[i + k] in datastream[i+k+1:i+n]:
                offset = k
                break
            else:
                found += 1
        if found == n:
            return i + n


if __name__ == '__main__':
    main()
