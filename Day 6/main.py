def part1():
    data = [int(d) for d in get_data()]

    for i in range(80):
        new_fish = []
        for i in range(len(data)):
            if data[i] == 0:
                data[i] = 6
                new_fish.append(8)
            else:
                data[i] -= 1
        data.extend(new_fish)

    return len(data)


def part2():
    data = [int(d) for d in get_data()]

    num_fish = len(data)
    fish_per_age = {i: 0 for i in range(9)}
    for d in data:
        fish_per_age[d] += 1

    for i in range(256):
        temp = {i: 0 for i in range(9)}
        for j in range(9):
            if j != 0:
                temp[j-1] += fish_per_age[j]
            else:
                temp[8] += fish_per_age[0]
                temp[6] += fish_per_age[0]
                num_fish += fish_per_age[0]
        fish_per_age = temp

    return num_fish


def get_data():
    with open("input.txt", "r") as f:
        return f.read().split(",")


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
