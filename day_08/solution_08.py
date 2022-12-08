import copy


def main():
    print("--- Day 8: Treetop Tree House ---")
    datastream_rows = [l.strip() for l in open('input.txt', 'r').readlines()]
    datastream_columns = [[copy.deepcopy(datastream_rows)[j][i] for j in range(
        len(datastream_rows))] for i in range(len(datastream_rows[0]))]
    print("Solution part 1: " + str(solve_part_1(copy.deepcopy(datastream_rows),
          copy.deepcopy(datastream_columns))))
    print("Solution part 2: " + str(solve_part_2(copy.deepcopy(datastream_rows),
          copy.deepcopy(datastream_columns))))


def solve_part_1(input_rows, input_columns):
    num_visible_trees = 0
    for row_index, trees in enumerate(input_rows):
        for column_index, tree in enumerate(trees):
            visible = True
            if column_index != 0 and row_index != 0 and column_index != (len(input_columns) - 1) and row_index != (len(input_rows) - 1):
                left = is_tree_visible_from_direction(
                    tree, get_trees_left_or_up_from_tree(column_index, trees))
                right = is_tree_visible_from_direction(
                    tree, get_trees_right_or_down_from_tree(column_index, trees))
                up = is_tree_visible_from_direction(tree, get_trees_left_or_up_from_tree(
                    row_index, input_columns[column_index]))
                down = is_tree_visible_from_direction(tree, get_trees_right_or_down_from_tree(
                    row_index, input_columns[column_index]))
                visible = left or right or up or down
            if (visible):
                num_visible_trees += 1
    return num_visible_trees


def solve_part_2(input_rows, input_columns):
    highest_tree_score = 0
    for row_index, trees in enumerate(input_rows):
        for column_index, tree in enumerate(trees):
            score = 0
            if column_index != 0 and row_index != 0 and column_index != (len(input_columns) - 1) and row_index != (len(input_rows) - 1):
                left = get_viewing_distance_for_direction(tree, list(
                    reversed(get_trees_left_or_up_from_tree(column_index, trees))))
                right = get_viewing_distance_for_direction(
                    tree, get_trees_right_or_down_from_tree(column_index, trees))
                up = get_viewing_distance_for_direction(tree, list(reversed(
                    get_trees_left_or_up_from_tree(row_index, input_columns[column_index]))))
                down = get_viewing_distance_for_direction(tree, get_trees_right_or_down_from_tree(
                    row_index, input_columns[column_index]))
                score = left * right * up * down
                if score > highest_tree_score:
                    highest_tree_score = score
    return highest_tree_score


def is_tree_visible_from_direction(tree_size, trees_in_that_direction):
    return tree_size > max(trees_in_that_direction)


def get_viewing_distance_for_direction(tree_size, trees_in_that_direction):
    if len(trees_in_that_direction) > 0:
        for index, tree in enumerate(trees_in_that_direction):
            if tree >= tree_size:
                return index + 1
        return len(trees_in_that_direction)
    return 0


def get_trees_left_or_up_from_tree(tree_index, row):
    return [t for i, t in enumerate(row) if i < tree_index]


def get_trees_right_or_down_from_tree(tree_index, row):
    return [t for i, t in enumerate(row) if i > tree_index]


if __name__ == '__main__':
    main()
