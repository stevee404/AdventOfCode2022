
def parse_input(path="input.txt"):
    with open(path, "r")as f:
        lines = f.readlines()

    elfs = list()

    elf = list()
    for line in lines:
        line = line.strip()

        if len(line) == 0:
            elfs.append(elf)
            elf = list()
            continue
        
        calories = int(line)
        elf.append(calories)
    
    return elfs

if __name__ == "__main__":
    elfs = parse_input()

    sum_elfs = [sum(elf) for elf in elfs]
    print("Max calories:", max(sum_elfs))

    top_three = sorted(sum_elfs, reverse=True)[:3]
    print("Top three:", sum(top_three))
