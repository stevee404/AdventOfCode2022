
def parse_input(path="input.txt"):
    with open(path, "r") as f:
        lines = f.readlines()
    
    areas = list()
    for line in lines:
        sections = line.split(",")
        area = list()
        for section in sections:
            section = section.split("-")
            area.append((int(section[0]), int(section[1])))
        areas.append(area)
    return areas


def fully_contained(areas: list):
    contained = 0
    for area in areas:
        a = area[0]
        b = area[1]
        if (
            a[0] <= b[0] <= b[1] <= a[1] 
            or b[0] <= a[0] <= a[1] <= b[1]
        ):
            contained += 1
    return contained
    

def overlaped(areas: list):
    overlap = 0
    for area in areas:
        a = area[0]
        b = area[1]
        if (
            a[0] <= b[0] <= a[1] <= b[1] or
            b[0] <= a[0] <= b[1] <= a[1] or
            a[0] <= b[0] <= b[1] <= a[1] or
            b[0] <= a[0] <= a[1] <= b[1]
        ):
            print(a,b)
            overlap += 1
    return overlap



if __name__ == "__main__":
    # test 1
    areas = parse_input("test.txt")
    contained = fully_contained(areas)
    assert(contained == 2)

    # puzzle 1
    areas = parse_input()
    contained = fully_contained(areas)
    print(contained)

    # test 2
    areas = parse_input("test.txt")
    overlap = overlaped(areas)
    assert(overlap == 4)

    # puzzle 2
    areas = parse_input()
    overlap = overlaped(areas)
    print(overlap)


