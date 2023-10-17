#!/usr/bin/env python3

import re
import pyllist


def main():
    print("--- Day 20: Grove Positioning System ---")
    input = tuple(open('input.txt', 'r').readlines())
    # print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    orig_dict = parse_input(input)
    dlist_nums = pyllist.dllist()
    for value in orig_dict.values():
        dlist_nums.append(value)

    for i in range(len(orig_dict)):
        item = orig_dict[i]
        dlist = mix(dlist_nums, item)
    print([d[1] for d in dlist])

    null_index = -1
    for i, node in enumerate(dlist):
        if dlist.nodeat(i).value[1] == 0:
            null_index = i
            break
    res = []
    res.append(dlist.nodeat((1000 + null_index) % len(dlist)).value[1])
    res.append(dlist.nodeat((2000 + null_index) % len(dlist)).value[1])
    res.append(dlist.nodeat((3000 + null_index) % len(dlist)).value[1])
    return sum(res)


def mix(dlist: pyllist.dllist, item_to_move):
    if item_to_move[1] != 0:
        old_list = list(dlist)
        index = old_list.index(item_to_move)
        item = dlist.nodeat(index)
        to_move = item_to_move[1]
        to_subtract = 0
        if (to_move < 0):
            to_subtract = -1
        to_subtract += int(to_move / len(dlist))
        if abs(to_move) > len(dlist):
            to_move = to_move % len(dlist)
        new_index = (index + to_move + to_subtract) % len(dlist)
        item_at_index = dlist.nodeat(new_index)
        dlist.remove(item)
        dlist.insert(x=pyllist.dllistnode(item_to_move), after=item_at_index)
        return dlist


def solve_part_2(input):
    orig_dict = parse_input(input)
    dlist_nums = pyllist.dllist()
    for value in orig_dict.values():
        dlist_nums.append(value)
    print([d[1] for d in dlist_nums])

    for _ in range(10):
        for i in range(len(orig_dict)):
            item = orig_dict[i]
            dlist = mix(dlist_nums, item)
        print([d[1] for d in dlist])

    null_index = -1
    for i, node in enumerate(dlist):
        if dlist.nodeat(i).value[1] == 0:
            null_index = i
            break
    res = []
    res.append(dlist.nodeat((1000 + null_index) % len(dlist)).value[1])
    res.append(dlist.nodeat((2000 + null_index) % len(dlist)).value[1])
    res.append(dlist.nodeat((3000 + null_index) % len(dlist)).value[1])
    return sum(res)


def parse_input(input):
    numbers = dict()
    for index, line in enumerate(input):
        n = re.findall('-?\d+\.?\d*', line)
        numbers[index] = (index, int(n[0]))
    return numbers


if __name__ == '__main__':
    main()
