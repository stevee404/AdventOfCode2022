import os

DIR = os.path.dirname(__file__)

def parse_input(path="input.txt"):
    with open(os.path.join(DIR, path), "r") as f:
        lines = f.readlines()
    return lines


def find_marker(datastream: str, unique_chars=4):
    for i in range(0, len(datastream)-unique_chars):
        marker = set(datastream[i:i+unique_chars])
        if len(marker) == unique_chars:
            return i+unique_chars


if __name__ == "__main__":
    # test 1
    datastreams = parse_input("test.txt")
    positions = [5, 6, 10, 11]
    for i in range(len(datastreams)):
        pos = find_marker(datastreams[i])
        print(positions[i], pos)
        assert(positions[i] == pos)

    # puzzle 1 
    datastream = parse_input()[0]
    pos = find_marker(datastream)
    print("paket marker", pos)

    # test 2
    positions = [23, 23, 29, 26]
    for i in range(len(datastreams)):
        pos = find_marker(datastreams[i], 14)
        print(positions[i], pos)
        assert(positions[i] == pos)

    # puzzle 2
    datastream = parse_input()[0]
    pos = find_marker(datastream, 14)
    print("message marker", pos)



