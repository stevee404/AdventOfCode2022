
def parse_input(path="input.txt"):
    with open(path, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines


def priority(letter: str):
    prio = ord(letter.lower()) - ord("a") + 1

    if letter == letter.upper():
        prio += 26
    
    return prio


def check_rucksacks(rucksacks: list):
    sum_prios = 0
    for rucksack in rucksacks:
        compartment_len = int(len(rucksack)/2)
        left = set(rucksack[:compartment_len])
        right = set(rucksack[compartment_len:])

        intersect = left.intersection(right)
        assert(len(intersect) == 1)
        
        letter = intersect.pop()
        sum_prios += priority(letter)

    return sum_prios


def get_badge(sack_1: str, sack_2: str, sack_3: str):
    badge = set(sack_1).intersection(set(sack_2))
    badge = badge.intersection(set(sack_3))
    assert(len(badge) == 1)
    return badge.pop()


def group_rucksacks(rucksacks: list):
    sum_badges = 0
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        badge = get_badge(*group)
        sum_badges += priority(badge)
    return sum_badges


if __name__ == "__main__":
    # test 1
    rucksacks = parse_input("test.txt")
    prios = check_rucksacks(rucksacks)
    print(prios)
    assert(prios == 157)

    # puzzle 1
    rucksacks = parse_input()
    prios = check_rucksacks(rucksacks)
    print(prios)

    # test 2
    rucksacks = parse_input("test.txt")
    badges = group_rucksacks(rucksacks)
    print(badges)

    # puzzle 2 
    rucksacks = parse_input()
    badges = group_rucksacks(rucksacks)
    print(badges)


