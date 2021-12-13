def part1():
    with open("input.txt") as f:
        course = f.readlines()

    horizontal, depth = 0, 0
    for entry in course:
        direction, distance = entry.split()
        if direction == "forward":
            horizontal += int(distance)
        elif direction == "down":
            depth += int(distance)
        elif direction == "up":
            depth -= int(distance)

    return horizontal * depth


def part2():
    with open("input.txt") as f:
        course = f.readlines()

    horizontal, depth, aim = 0, 0, 0
    for entry in course:
        direction, distance = entry.split()
        if direction == "forward":
            horizontal += int(distance)
            depth += int(distance) * aim
        elif direction == "down":
            aim += int(distance)
        elif direction == "up":
            aim -= int(distance)

    return horizontal * depth


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
