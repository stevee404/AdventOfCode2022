
def parse_input(path="input.txt"):
    with open(path, "r") as f:
        lines = f.readlines()

    rounds = [line.split() for line in lines]
    return rounds

SHAPE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3
}

def game_logic(rounds):
    score = 0
    for _round in rounds:
        round_score = 0
        shapes = "".join(str(shape) for shape in _round)

        # win
        if (
            shapes == "AY" or
            shapes == "BZ" or
            shapes == "CX"
        ):
            round_score += 6
        # draw
        elif (
            shapes == "AX" or
            shapes == "BY" or
            shapes == "CZ"
        ):
            round_score += 3

        round_score += SHAPE_SCORE[_round[1]]
        score += round_score
    
    return score


WIN_SHAPE = {
    "A": "B",
    "B": "C",
    "C": "A"
}

def game_logic2(rounds):
    score = 0

    for _round in rounds:
        round_score = 0
        strategy = _round[1]
        opponent = _round[0]

        # win
        if strategy == "Z":
            round_score += 6
            shape = WIN_SHAPE[opponent]
            round_score += SHAPE_SCORE[shape]

        # draw
        if strategy == "Y":
            round_score += 3
            round_score += SHAPE_SCORE[opponent]

        # lose
        if strategy == "X":
            shape = WIN_SHAPE[WIN_SHAPE[opponent]]
            round_score += SHAPE_SCORE[shape]
        
        score += round_score
    return score


if __name__ == "__main__":
    # test 1
    rounds = parse_input(path="test.txt")
    test_score = int(rounds[0][0])
    score = game_logic(rounds[1:])
    print(test_score, score)
    assert(test_score == score)
    
    # puzzle 1
    rounds = parse_input()
    score = game_logic(rounds)
    print("Strategy 1 Score", score)

    # test 2
    rounds = parse_input(path="test2.txt")
    test_score = int(rounds[0][0])
    score = game_logic2(rounds[1:])
    print(test_score, score)
    assert(test_score == score)

    # puzzle 2
    rounds = parse_input()
    score = game_logic2(rounds)
    print("Strategy 2 Score:", score)

