import string


def main():
    print("--- Day 3: Rucksack Reorganization ---")
    input = open('input.txt', 'r')
    prio_list = getPriorityList()
    solve_part_1(input, prio_list)
    solve_part_2(input.readlines(), prio_list)


def solve_part_1(input, prio_list):
    prio_sum = 0
    for line in input:
        left, right = getRucksackCompartmentItems(line.replace('\n', ''))
        intersection = list(set(left) & set(right))[0]
        prio_sum += prio_list.index(intersection) + 1
        print(left)
        print(right)
        print("Duplicate item: " + intersection + ", Priority: " +
              str(prio_list.index(intersection) + 1))
    print(str(prio_sum))


def getPriorityList():
    list = []
    for i in string.ascii_lowercase:
        list.append(i)
    for i in string.ascii_uppercase:
        list.append(i)
    return list


def getRucksackCompartmentItems(items):
    left = [*items[0:len(items)//2]]
    right = [*items[len(items)//2:]]
    return left, right


def solve_part_2(lines, prio_list):
    prio_sum = 0
    for i in range(0, int(len(lines)/3)):
        one = [*lines[i * 3].replace('\n', '')]
        two = [*lines[i * 3 + 1].replace('\n', '')]
        three = [*lines[i * 3 + 2].replace('\n', '')]
        intersection = list(set(one) & set(two) & set(three))[0]
        prio_sum += prio_list.index(intersection) + 1
        print("Group: " + str(i))
        print(one)
        print(two)
        print(three)
        print("Badge item: " + intersection + ", Priority: " +
              str(prio_list.index(intersection) + 1))
        print("---")
    print(str(prio_sum))


if __name__ == '__main__':
    main()
