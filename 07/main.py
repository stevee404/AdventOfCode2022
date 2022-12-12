import os

DIR = os.path.dirname(__file__)

def parse_input(path="input.txt"):
    lines = list()
    with open(os.path.join(DIR, path)) as f:
        for line in f:
            lines.append(line.strip())
    return lines


def traverse_dirs(lines: list):
    pwd = list()
    dirs = dict()
    
    for line in lines:
        if line.startswith("$ cd"):
            _dir = line.split()[2]
            if _dir == "..":
                pwd.pop(-1)
            elif _dir == "/":
                pwd = ["/"]
            else:
                pwd.append(_dir)
        
        elif line.startswith("$ ls") or line.startswith("dir"):
            continue
        else:
            size, filename = line.split()
            for _dir in pwd:
                if _dir not in dirs:
                    dirs[_dir] = 0
                dirs[_dir] += int(size)
    return dirs


def filter_dirs(dirs: dict, max_size=100_000):
    filtered = list(filter(lambda item: item[1] <= max_size, dirs.items()))
    sizes = [item[1] for item in filtered]
    return filtered, sum(sizes)


if __name__ == "__main__":
    # test 1
    lines = parse_input("test.txt")
    dirs = traverse_dirs(lines)
    print(dirs)
    filtered, sizes = filter_dirs(dirs)
    print(filtered, sizes)
    assert(sizes == 95437)

    # puzzle 1
    lines = parse_input()
    dirs = traverse_dirs(lines)
    filtered, sizes = filter_dirs(dirs)
    print(filtered, sizes)
    