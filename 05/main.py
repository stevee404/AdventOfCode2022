import os

DIR = os.path.dirname(__file__)

def parse_input(filename="input.txt"):
    with open(os.path.join(DIR, filename), "r") as f:
        crates = list()
        line = f.readline()
        while (len(line.strip()) != 0):
            crates.append(line)
            line = f.readline()
        
        instructions = f.readlines()

    # parse crates & stack
    stacks = list()
    for line in crates[:-1]:
        for i in range(0, len(line), 4):
            idx = int(i / 4)
            
            # add new stack
            if idx >= len(stacks):
                stacks.append(list())
            
            # add crate to stack
            crate = line[i:i+4].strip()
            if len(crate) > 0:
                stacks[idx].insert(0, crate[1])

    # parse instrunctions
    instructs = list()
    for line in instructions:
        split = line.split()
        instruct = [int(split[1]), int(split[3])-1, int(split[5])-1]
        instructs.append(instruct)
    
    return stacks, instructs


def move_crates(stacks, instructions):
    for instruct in instructions:
        num_crates,from_stack, to_stack = instruct
        
        for i in range(num_crates):
            crate = stacks[from_stack].pop(-1)
            stacks[to_stack].append(crate)


def move_crates2(stacks, instructions):
    for instruct in instructions:
        num_crates,from_stack, to_stack = instruct
        
        for i in range(num_crates, 0, -1):
            crate = stacks[from_stack].pop(-i)
            stacks[to_stack].append(crate)


def get_top_crates(stacks):
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1]
    return top_crates

if __name__ == "__main__":
    # test 1
    stacks, instructs = parse_input("test.txt")
    move_crates(stacks, instructs)
    top_crates = get_top_crates(stacks)
    print(top_crates)
    assert(top_crates == "CMZ")

    # puzzle 1
    stacks, instructs = parse_input()
    move_crates(stacks, instructs)
    top_crates = get_top_crates(stacks)
    print(top_crates)
    
    # test 2
    stacks, instructs = parse_input("test.txt")
    move_crates2(stacks, instructs)
    top_crates = get_top_crates(stacks)
    print(top_crates)
    assert(top_crates == "MCD")

    # puzzle 2
    stacks, instructs = parse_input()
    move_crates2(stacks, instructs)
    top_crates = get_top_crates(stacks)
    print(top_crates)



