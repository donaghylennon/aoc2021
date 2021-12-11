import sys
import math


def part1():
    crabs = get_data()

    min_distance = sys.maxsize
    for i in range(max(crabs)):
        sum_distances = 0
        for crab in crabs:
            sum_distances += abs(crab - i)
        if sum_distances < min_distance:
            min_distance = sum_distances

    return min_distance


def part2():
    crabs = get_data()

    min_fuel = sys.maxsize
    for i in range(max(crabs)):
        sum_fuel = 0
        for crab in crabs:
            sum_fuel += sum([j for j in range(abs(crab - i) + 1)])
        if sum_fuel < min_fuel:
            min_fuel = sum_fuel

    return min_fuel


def get_data():
    with open("input.txt", "r") as f:
        return [int(d) for d in f.read().split(",")]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
