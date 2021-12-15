from copy import copy


class Node:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections


def part1():
    pairs = [line.strip().split("-") for line in get_data()]

    connections = {}
    for pair in pairs:
        if connections.get(pair[0]) != None:
            connections[pair[0]].append(pair[1])
        else:
            connections[pair[0]] = [pair[1]]
        if connections.get(pair[1]) != None:
            connections[pair[1]].append(pair[0])
        else:
            connections[pair[1]] = [pair[0]]
    # print(connections)

    return len(visit("start", connections, []))


def visit(cave, connections, small_caves):
    paths = []
    sc = copy(small_caves)
    if all(char.islower() for char in cave):
        if any(cave == c for c in small_caves):
            return None
        sc.append(cave)

    for con_cave in connections[cave]:
        if con_cave == "end":
            paths.append([con_cave])
        else:
            connected_paths = visit(con_cave, connections, sc)
            if not connected_paths is None:
                paths.extend([p for p in connected_paths if p != None])

    for path in paths:
        path.append(cave)

    return paths


def visit2(cave, connections, small_caves):
    paths = []
    sc = copy(small_caves)
    if all(char.islower() for char in cave):
        sc.append(cave)
    repeats = 0
    for i, c1 in enumerate(sc):
        for j, c2 in enumerate(sc):
            if i == j:
                continue
            if c1 == c2:
                if c1 == "start" or c1 == "end":
                    return None
                repeats += 1
    if repeats > 2:
        return None

    for con_cave in connections[cave]:
        if con_cave == "end":
            paths.append([con_cave])
        else:
            connected_paths = visit2(con_cave, connections, sc)
            if not connected_paths is None:
                paths.extend([p for p in connected_paths if p != None])

    for path in paths:
        path.append(cave)

    return paths


def part2():
    pairs = [line.strip().split("-") for line in get_data()]

    connections = {}
    for pair in pairs:
        if connections.get(pair[0]) != None:
            connections[pair[0]].append(pair[1])
        else:
            connections[pair[0]] = [pair[1]]
        if connections.get(pair[1]) != None:
            connections[pair[1]].append(pair[0])
        else:
            connections[pair[1]] = [pair[0]]

    return len(visit2("start", connections, []))


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
