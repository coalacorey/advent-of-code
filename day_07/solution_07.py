def main():
    print("--- Day 7: No Space Left On Device ---")
    input = open('input.txt', 'r').readlines()
    # print_file_tree("/", get_dir_tree(input), 0)
    print("Solution part 1: " + str(solve_part_1(input)))
    print("Solution part 2: " + str(solve_part_2(input)))


def solve_part_1(terminal_output):
    dir_tree = get_dir_tree(terminal_output)
    dirs_with_size = {}
    for dir in dir_tree:
        dirs_with_size[dir] = calc_dir_size(dir, dir_tree)
    dirs_below_threshold = get_dirs_with_size_below_threshold(
        dirs_with_size, 100000)
    res = sum([dirs_with_size[dir] for dir in dirs_below_threshold])
    return res


def solve_part_2(terminal_output):
    dir_tree = get_dir_tree(terminal_output)
    total_disk_space = 70000000
    required_space = 30000000
    root_size = calc_dir_size("/", dir_tree)
    to_delete_space = required_space - (total_disk_space - root_size)
    dirs_with_size = {}
    for dir in dir_tree:
        dirs_with_size[dir] = calc_dir_size(dir, dir_tree)
    sorted_dirs_by_value = sorted(dirs_with_size.items(), key=lambda x: x[1])
    dirs_above_threshold = get_dirs_with_size_above_threshold(
        sorted_dirs_by_value, to_delete_space)
    return dirs_above_threshold


def get_dir_tree(commands):
    # Saves all the directories with their files and a list of sub-directories
    dict_tree = {}
    # Terminal lines that result from calling ls in directory x
    directory_contents_terminal = []
    current_path = ""
    # Keeps track of if the last $ command was a ls command
    ls_mode = False
    for line in commands:
        l = line.split()
        # If we have a $ command we either change the directory or list its contents
        if l[0] == '$':
            if l[1] == "cd":
                # If we previously listed all the directory contents with ls and
                # want to cd to another directory we add that ls output to the
                # directory tree
                if ls_mode:
                    dir_contents = ls(
                        current_path, directory_contents_terminal)
                    dict_tree[current_path]["f"] = dir_contents["f"]
                    dict_tree[current_path]["d"] = dir_contents["d"]
                current_path = cd(current_path, l[2])
                # If we are moving into a unseen directory we add it to the dict_tree
                if l[2] != "..":
                    if current_path not in dict_tree:
                        dict_tree[current_path] = empty_dir_dict()
                # When we leave the directory the ls mode and directory_contents reset
                directory_contents_terminal = []
                ls_mode = False
            if l[1] == "ls":
                ls_mode = True
        # Otherwise the line describes a file or directory
        else:
            if ls_mode:
                directory_contents_terminal.append(line.replace('\n', ''))
    return dict_tree


def empty_dir_dict():
    dict = {}
    dict["f"] = {}
    dict["d"] = []
    return dict


def cd(current_path, directory):
    new_path = ""
    if directory == "/":
        new_path = "/"
    elif directory == "..":
        new_path = current_path[:current_path.rindex("/")]
        if new_path == "":
            new_path = "/"
    elif directory.isalpha():
        if current_path == "/":
            new_path = "/" + directory
        else:
            new_path = current_path + "/" + directory
    return new_path


def ls(path, output):
    # Dict of directories and files
    dir_contents = {}
    # Dict of directories
    directories = []
    # Dict of files with their sizes
    files = {}

    for line in output:
        l = line.split()
        # if first part of command is a digit we have a file
        if l[0].isdigit():
            # Add file with size to dict, e.g. {foo.txt, 123}
            files[l[1]] = int(l[0])
        # Otherwise the command shows a directory
        else:
            directories.append(cd(path, l[1]))
    dir_contents["f"] = files
    dir_contents["d"] = directories
    return dir_contents


def directory_size_files(files):
    return sum(list(files.values()))


def calc_dir_size(current_dir, dir_dict):
    if current_dir in dir_dict:
        file_size = directory_size_files(dir_dict[current_dir]["f"])
        dir_size = 0
        for dir in dir_dict[current_dir]["d"]:
            if dir in dir_dict:
                dir_size += calc_dir_size(dir, dir_dict)
        return dir_size + file_size
    else:
        return 0


def print_file_tree(directory, dir_dict, level):
    sep = ""
    size = calc_dir_size(directory, dir_dict)
    print(sep + directory + " : " + str(size))
    if directory in dir_dict:
        for f in dir_dict[directory]["f"]:
            print(sep + directory + "/[" + f + "] : " +
                  str(dir_dict[directory]["f"][f]))
        for d in dir_dict[directory]["d"]:
            print_file_tree(d, dir_dict, level + 1)


def get_dirs_with_size_below_threshold(dirs, threshold):
    res = []
    for dir in dirs:
        if dirs[dir] <= threshold:
            res.append(dir)
    return res


def get_dirs_with_size_above_threshold(dirs, threshold):
    res = []
    for dir in dirs:
        if dir[1] >= threshold:
            res.append(dir)
    return res


if __name__ == '__main__':
    main()
