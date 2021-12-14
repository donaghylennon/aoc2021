from itertools import product


def part1():
    grid = [[int(c) for c in line.strip()] for line in get_data()]
    coords = (-1, 0, 1)

    num_flashes = 0
    nrows = len(grid)
    ncols = len(grid[0])
    for _ in range(100):
        for row in range(nrows):
            for col in range(ncols):
                grid[row][col] += 1
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] > 9:
                    num_flashes += 1
                    grid[row][col] = 0

                    to_visit = [(row + r, col + c)
                                for r, c in product(coords, coords)]
                    i = 0
                    while i < len(to_visit):
                        new_row, new_col = to_visit[i]
                        if 0 <= new_row <= nrows-1 and 0 <= new_col <= ncols-1:
                            if grid[new_row][new_col] != 0:
                                grid[new_row][new_col] += 1
                                if grid[new_row][new_col] > 9:
                                    num_flashes += 1
                                    grid[new_row][new_col] = 0
                                    to_visit.extend([(new_row + r, new_col + c)
                                                     for r, c in product(coords, coords)])
                        i += 1

    return num_flashes


def part2():
    grid = [[int(c) for c in line.strip()] for line in get_data()]
    coords = (-1, 0, 1)

    num_flashes = 0
    nrows = len(grid)
    ncols = len(grid[0])
    for step in range(500):
        for row in range(nrows):
            for col in range(ncols):
                grid[row][col] += 1
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] > 9:
                    num_flashes += 1
                    grid[row][col] = 0

                    to_visit = [(row + r, col + c)
                                for r, c in product(coords, coords)]
                    i = 0
                    while i < len(to_visit):
                        new_row, new_col = to_visit[i]
                        if 0 <= new_row <= nrows-1 and 0 <= new_col <= ncols-1:
                            if grid[new_row][new_col] != 0:
                                grid[new_row][new_col] += 1
                                if grid[new_row][new_col] > 9:
                                    num_flashes += 1
                                    grid[new_row][new_col] = 0
                                    to_visit.extend([(new_row + r, new_col + c)
                                                     for r, c in product(coords, coords)])
                        i += 1
        sync_flash = True
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] != 0:
                    sync_flash = False
        if sync_flash:
            return step + 1
    return -1


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
