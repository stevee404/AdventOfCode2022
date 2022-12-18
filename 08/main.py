import os

DIR = os.path.dirname(__file__)

def parse_input(filename="input.txt"):
    with open(os.path.join(DIR, filename), "r") as f:
        lines = f.readlines()
    
    forest = list()
    for line in lines:
        line = line.strip()
        trees = [int(tree) for tree in list(line)]
        forest.append(trees)
    return forest


def find_visible_trees(forest: list):
    # edges
    visible = (len(forest) + len(forest[0])) * 2
    visible -= 4
    print(visible)

    # inners trees
    for row in range(1, len(forest)-1):
        for column in range(1, len(forest[0])-1):
            tree = forest[row][column]
            hidden = 0
            # top
            for i in range(0, row):
                if forest[i][column] >= tree:
                    hidden +=1
                    break
            # bottom
            for i in range(row+1, len(forest)):
                if forest[i][column] >= tree:
                    hidden +=1
                    break
            # left
            for i in range(0, column):
                if forest[row][i] >= tree:
                    hidden +=1
                    break
            # right
            for i in range(column+1, len(forest[row])):
                if forest[row][i] >= tree:
                    hidden += 1
                    break

            if hidden < 4:
                # print(column, row, tree)
                visible += 1
    return visible

def mult(iterable):
    ret = 1
    for i in iterable:
        ret *= i
    return ret


def find_best_view():
    best_scenic_values = list()
    best_scenic_score = 0
    for row in range(0, len(forest)):
        for column in range(1, len(forest[0])):
            scenic_values = list()
            tree = forest[row][column]

            distance = 0
            # top
            for i in range(row, 0, -1):
                if forest[i][column] < tree:
                    distance +=1
                else:
                    break
            scenic_values.append(distance)
            # bottom
            for i in range(row+1, len(forest)):
                if forest[i][column] >= tree:
                    hidden +=1
                    break
            # left
            for i in range(0, column):
                if forest[row][i] >= tree:
                    hidden +=1
                    break
            # right
            for i in range(column+1, len(forest[row])):
                if forest[row][i] >= tree:
                    hidden += 1
                    break

            if hidden < 4:
                # print(column, row, tree)
                visible += 1
    return visible


if __name__ == "__main__":
    # test 1 
    forest = parse_input("test.txt")
    visible = find_visible_trees(forest)
    print(visible)
    
    # puzzle 1
    forest = parse_input()
    visible = find_visible_trees(forest)
    print(visible)