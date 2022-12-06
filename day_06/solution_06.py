def main():
    print("--- Day 5: Supply Stacks ---")
    datastream = open('input.txt', 'r').readlines()[0]
    print("Solution part 1: " + str(solve_part_1(datastream)))
    print("Solution part 2: " + str(solve_part_2(datastream)))


def solve_part_1(datastream):
    return find_index_of_first_n_distinct_characters(datastream, 4)


def solve_part_2(datastream):
    return find_index_of_first_n_distinct_characters(datastream, 14)


# We start with index i and a list from k (= k+i) to i+n, if i is in that list we increase the indeces i (and therefore k and n).
# If i is not in that list we increase index k and look if the new character is within the remaining list.
# With each iteration the remaining list is smaller and after n - 1 comparisons the index is found.
def find_index_of_first_n_distinct_characters(datastream, n):
    for i in range(0, len(datastream) - n + 1):
        if len([True for k in range(0, n - 1) if datastream[i + k] not in datastream[i+k+1:i+n]]) == n - 1:
            return i + n


if __name__ == '__main__':
    main()
