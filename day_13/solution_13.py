#!/usr/bin/env python3
import copy
import functools


def main():
    print("--- Day 13: Distress Signal ---")
    datastream = open('input.txt', 'r').readlines()
    print("Solution part 1: " + str(solve_part_1(copy.deepcopy(datastream))))
    print("Solution part 2: " + str(solve_part_2(copy.deepcopy(datastream))))


def solve_part_1(datastream) -> int:
    signal_pairs = []
    i = 0
    while i in range(len(datastream) - 1):
        pair = []
        pair.append(eval(str(datastream[i].strip())))
        pair.append(eval(str(datastream[i + 1].strip())))
        signal_pairs.append(pair)
        i += 3

    sum = 0
    for index, pair in enumerate(signal_pairs):
        if compare_pair_ordering(pair[0], pair[1]) == 1:
            sum += index + 1
    return sum


def solve_part_2(datastream):
    signal_pairs = []
    for i in range(len(datastream)):
        if len(datastream[i].strip()) > 0:
            signal_pairs.append(eval(str(datastream[i].strip())))

    signal_pairs.append([[2]])
    signal_pairs.append([[6]])

    s = sorted(signal_pairs, key=functools.cmp_to_key(
        compare_pair_ordering), reverse=True)
    index_1 = s.index([[2]]) + 1
    index_2 = s.index([[6]]) + 1
    return index_1*index_2


def compare_pair_ordering(in_left, in_right):
    left = copy.deepcopy(in_left)
    right = copy.deepcopy(in_right)
    # Check if left list is not empty
    while len(left) > 0:
        # Check if right list is not empty, otherwise return false because it ran out of list elements first
        if right:
            # Since left and right are not emtpy they have at least one item
            l = left[0]
            r = right[0]
            # Check if both values are integers
            if isinstance(l, int) and isinstance(r, int):
                # If left int is smaller ordering is correct
                if l < r:
                    return 1
                # If right int is smaller ordering is false
                elif l > r:
                    return - 1
                # If they are the same move on to the next list element
                else:
                    left.pop(0)
                    right.pop(0)
                    continue
            # Check if both values are lists, in that case we start recursion
            elif isinstance(l, list) and isinstance(r, list):
                inner_ordering = compare_pair_ordering(l, r)
                # If the inner ordering could not be determined we remove the lists and continue
                if inner_ordering == 0:
                    left.pop(0)
                    right.pop(0)
                    continue
                else:
                    return inner_ordering
            # One value is a list, the other an integer, so put the int into a list
            elif type(l) != type(r):
                if isinstance(l, int):
                    left[0] = [l]
                elif isinstance(r, int):
                    right[0] = [r]
        else:
            # If right list is empty before left list return false
            return - 1
    # If the lists have the same length and are empty there can be made no statement about the ordering (happens only in recursion!)
    if len(left) == len(right):
        return 0
    # If only the left list is empty return true
    else:
        return 1


if __name__ == '__main__':
    main()
