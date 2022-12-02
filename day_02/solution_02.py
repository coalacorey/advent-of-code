selection_dict = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
mapping_dict = {"A": "Rock", "B": "Paper", "C": "Scissors",
                "X": "Rock", "Y": "Paper", "Z": "Scissors"}
outcome_dict = {"X": "Loss", "Y": "Draw", "Z": "Win"}
outcome_selection_dict = {"XA": "Z", "XB": "X", "XC": "Y",
                          "YA": "X", "YB": "Y", "YC": "Z", "ZA": "Y", "ZB": "Z", "ZC": "A"}


def main(part):
    print("Rock, Paper, Scissors!")
    input = open('input.txt', 'r')
    score = 0
    round = 1
    for line in input:
        print("Round " + str(round))
        round_score = calculate_round_score(line.split(), part)
        print("Score: " + str(round_score))
        score += round_score
        round += 1
    print("Final score: " + str(score))


def calculate_round_score(splitted_line, part):
    if part == 1:
        return calculate_selection_score(splitted_line[1]) + calculate_result_score(splitted_line[0], splitted_line[1])
    if part == 2:
        selection = outcome_selection_dict[splitted_line[1] + splitted_line[0]]
        print("Chose " + mapping_dict[selection] + " to force a " +
          outcome_dict[splitted_line[1]] + " against " + mapping_dict[splitted_line[0]])
        return calculate_selection_score(selection) + calculate_result_score(splitted_line[0], selection)


def calculate_selection_score(selection):
    print(str(selection_dict[selection]) +
          " point(s) for selecting " + mapping_dict[selection])
    return selection_dict[selection]


def calculate_result_score(opponent, selection):
    diff = selection_dict[opponent] - selection_dict[selection]
    if diff == 0:
        print("3 points for draw! Both chose " + mapping_dict[opponent])
        return 3
    if (diff == 1 or diff == -2):
        print("0 points. " +
              mapping_dict[selection] + " loses to " + mapping_dict[opponent])
        return 0
    if (diff == -1 or diff == 2):
        print("6 points! " +
              mapping_dict[selection] + " beats " + mapping_dict[opponent])
        return 6


if __name__ == '__main__':
    main(2)
