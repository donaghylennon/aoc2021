def part1():
    coords = []
    coords = set()
    folds = []
    data = get_data()
    parse_folds = False
    for line in data:
        line = line.strip()
        if line == "":
            parse_folds = True
            continue
        if not parse_folds:
            x, y = line.split(",")
            x, y = int(x), int(y)
            coords.add((x, y))
        else:
            axis, dist = line.split()[2].split("=")
            dist = int(dist)
            folds.append((axis, dist))

    new_coords = set()
    fold = folds[0]
    if fold[0] == 'x':
        for coord in coords:
            if coord[0] > fold[1]:
                new_coords.add((2*fold[1] - coord[0], coord[1]))
            else:
                new_coords.add(coord)
    elif fold[0] == 'y':
        for coord in coords:
            if coord[1] > fold[1]:
                new_coords.add((coord[0], 2*fold[1] - coord[1]))
            else:
                new_coords.add(coord)
    return len(new_coords)


def part2():
    coords = []
    coords = set()
    folds = []
    data = get_data()
    parse_folds = False
    for line in data:
        line = line.strip()
        if line == "":
            parse_folds = True
            continue
        if not parse_folds:
            x, y = line.split(",")
            x, y = int(x), int(y)
            coords.add((x, y))
        else:
            axis, dist = line.split()[2].split("=")
            dist = int(dist)
            folds.append((axis, dist))

    fold = folds[0]
    for fold in folds:
        new_coords = set()
        if fold[0] == 'x':
            for coord in coords:
                if coord[0] > fold[1]:
                    new_coords.add((2*fold[1] - coord[0], coord[1]))
                else:
                    new_coords.add(coord)
        elif fold[0] == 'y':
            for coord in coords:
                if coord[1] > fold[1]:
                    new_coords.add((coord[0], 2*fold[1] - coord[1]))
                else:
                    new_coords.add(coord)
        coords = new_coords

    max_x = 0
    max_y = 0
    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
    output_lists = []
    for y in range(max_y + 3):
        opl = []
        for x in range(max_x + 3):
            opl.append(".")
        output_lists.append(opl)
    for coord in coords:
        output_lists[coord[1]][coord[0]] = '#'

    return "\n".join("".join(ls) for ls in output_lists)


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
