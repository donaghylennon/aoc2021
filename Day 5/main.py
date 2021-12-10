def part1():
    data = [d.split(" -> ") for d in get_data()]
    data = [(d[0].split(","), d[1].split(",")) for d in data]
    data = [
        ((int(d[0][0]), int(d[0][1])), (int(d[1][0]), int(d[1][1]))) for d in data
        if d[0][0] == d[1][0] or d[0][1] == d[1][1]
    ]

    grid = {}
    for d in data:
        stepx = 1 if d[1][0] > d[0][0] else -1
        stepy = 1 if d[1][1] > d[0][1] else -1
        for x in range(d[0][0], d[1][0], stepx):
            for y in range(d[0][1], d[1][1], stepy):
                key = (x, y)
                grid[key] = grid.get(key, 0) + 1
        if d[0][0] > d[1][0]:
            for x in range(d[1][0], d[0][0] + 1):
                key = (x, d[0][1])
                grid[key] = grid.get(key, 0) + 1
        elif d[1][0] > d[0][0]:
            for x in range(d[0][0], d[1][0] + 1):
                key = (x, d[0][1])
                grid[key] = grid.get(key, 0) + 1
        elif d[0][1] > d[1][1]:
            for y in range(d[1][1], d[0][1] + 1):
                key = (d[0][0], y)
                grid[key] = grid.get(key, 0) + 1
        elif d[1][1] > d[0][1]:
            for y in range(d[0][1], d[1][1] + 1):
                key = (d[0][0], y)
                grid[key] = grid.get(key, 0) + 1

    number_overlap = 0
    for overlap in grid.values():
        if overlap >= 2:
            number_overlap += 1

    return number_overlap


def part2():
    data = [d.split(" -> ") for d in get_data()]
    data = [(d[0].split(","), d[1].split(",")) for d in data]
    data = [((int(d[0][0]), int(d[0][1])), (int(d[1][0]), int(d[1][1])))
            for d in data]

    grid = {}
    for d in data:
        stepx = 1 if d[1][0] >= d[0][0] else -1
        stepy = 1 if d[1][1] >= d[0][1] else -1
        x_coords = range(d[0][0], d[1][0] + stepx, stepx) if d[0][0] != d[1][0]\
            else [d[0][0]] * (abs(d[1][1] - d[0][1]) + 1)
        y_coords = range(d[0][1], d[1][1] + stepy, stepy) if d[0][1] != d[1][1]\
            else [d[0][1]] * (abs(d[1][0] - d[0][0]) + 1)
        for x, y in zip(x_coords, y_coords):
            key = (x, y)
            grid[key] = grid.get(key, 0) + 1

    number_overlap = 0
    for overlap in grid.values():
        if overlap >= 2:
            number_overlap += 1

    return number_overlap


def get_data():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
