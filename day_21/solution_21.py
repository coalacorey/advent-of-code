#!/usr/bin/env python3
import re
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def main():
    print("--- Day 21: Monkey Math ---")
    input = tuple(open('input.txt', 'r').readlines())
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(input):
    monkey_dict = parse_input(input)
    monkey_tree = build_tree(monkey_dict, "root")
    return solve_tree(monkey_dict, monkey_tree, dict())


def solve_part_2(input):
    return 0


def parse_input(input):
    monkey_dict = dict()
    for line in input:
        # By default a monkey is associated with a number that he yells
        operation = '#'
        if "+" in line:
            operation = "+"
        if "-" in line:
            operation = "-"
        if "*" in line:
            operation = "*"
        if "/" in line:
            operation = "/"
        left = ""
        # By default the number a monkey yells, left/right (monkey) is set to None
        number, left, right = None, None, None
        # Finds digits in a string
        n = re.findall('-?\d+\.?\d*', line)
        # If there is a digit, the monkey yells it out
        if len(n) > 0:
            number = int(n[0])
        monkeys_involved = re.findall(r"\b[a-z]{4}\b", line)
        main_monkey = monkeys_involved[0]
        if len(monkeys_involved) == 3:
            left = monkeys_involved[1]
            right = monkeys_involved[2]
        m = (operation, number, left, right)
        monkey_dict[main_monkey] = m
    return monkey_dict


def build_tree(monkeys: dict, monkey_name) -> Node:
    monkey = monkeys[monkey_name]
    current_node = Node(monkey_name)
    if monkey[0] == "#":
        node = Node(monkey_name)
        return node
    else:
        left, right = monkey[2], monkey[3]
        current_node.left = build_tree(monkeys, left)
        current_node.right = build_tree(monkeys, right)
    return current_node


def solve_tree(monkeys: dict, monkey_node: Node, res: dict):
    monkey = monkeys[monkey_node.data]
    if monkey[0] == "#":
        res[monkey_node.data] = monkey[1]
        return monkey[1]
    else:
        left, right = solve_tree(monkeys, monkey_node.left, res), solve_tree(monkeys, monkey_node.right, res)
        op_res = int(ops[monkey[0]](left, right))
        res[monkey_node.data] = op_res
        return op_res


if __name__ == '__main__':
    main()
