def part1():
    with open("input.txt", "r") as f:
        data = [l.strip() for l in f.readlines()]

    nbits = len(data[0])
    num_ones = {i: 0 for i in range(nbits)}
    for line in data:
        for i in range(nbits):
            if line[i] == "1":
                num_ones[i] += 1

    result = ""
    for i in range(nbits):
        if num_ones[i] > len(data)/2:
            result += "1"
        else:
            result += "0"

    gamma = int(result, 2)
    mask = 1
    for i in range(nbits-1):
        mask <<= 1
        mask |= 1
    epsilon = (~gamma) & mask

    return gamma * epsilon


def part2():
    with open("input.txt", "r") as f:
        data = [l.strip() for l in f.readlines()]

    nbits = len(data[0])
    oxygen_values = []
    co2_values = []
    for line in data:
        oxygen_values.append(line)
        co2_values.append(line)

    for i in range(nbits):
        if len(oxygen_values) == 1:
            break
        current_length = len(oxygen_values)
        num_ones = 0
        for line in oxygen_values:
            if line[i] == "1":
                num_ones += 1
        next_gen = []
        for line in oxygen_values:
            if len(oxygen_values) == 1:
                break
            if num_ones >= current_length/2:
                if line[i] != "0":
                    next_gen.append(line)
            else:
                if line[i] != "1":
                    next_gen.append(line)
        oxygen_values = next_gen

    for i in range(nbits):
        if len(co2_values) == 1:
            break
        current_length = len(co2_values)
        num_ones = 0
        for line in co2_values:
            if line[i] == "1":
                num_ones += 1
        next_gen = []
        for line in co2_values:
            if len(co2_values) == 1:
                break
            if num_ones < current_length/2:
                if line[i] != "0":
                    next_gen.append(line)
            else:
                if line[i] != "1":
                    next_gen.append(line)
        co2_values = next_gen

    oxygen = int(oxygen_values[0], 2)
    co2 = int(co2_values[0], 2)

    return oxygen * co2


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
