def part1():
    heightmap = [[int(p) for p in line] for line in get_data()]

    sum_risk_levels = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            is_low_point = True
            point = heightmap[i][j]
            if i > 0 and not point < heightmap[i-1][j]:
                is_low_point = False
            if i < len(heightmap)-1 and not point < heightmap[i+1][j]:
                is_low_point = False
            if j > 0 and not point < heightmap[i][j-1]:
                is_low_point = False
            if j < len(heightmap[i])-1 and not point < heightmap[i][j+1]:
                is_low_point = False

            if is_low_point:
                sum_risk_levels += point + 1

    return sum_risk_levels


def part2():
    heightmap = [[int(p) for p in line] for line in get_data()]
    visited = [[False for j in range(len(line))] for line in heightmap]

    largest_basins = [0, 0, 0]
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            if visited[i][j]:
                continue
            is_low_point = True
            point = heightmap[i][j]
            if i > 0:
                if not point < heightmap[i-1][j]:
                    is_low_point = False
            if i < len(heightmap)-1:
                if not point < heightmap[i+1][j]:
                    is_low_point = False
            if j > 0:
                if not point < heightmap[i][j-1]:
                    is_low_point = False
            if j < len(heightmap[i])-1:
                if not point < heightmap[i][j+1]:
                    is_low_point = False

            if not is_low_point:
                continue
            points_to_visit = [(i, j)]
            visited[i][j] = True
            basin_size = 0
            index = 0
            while index < len(points_to_visit):
                x, y = points_to_visit[index]
                index += 1
                if heightmap[x][y] == 9:
                    continue
                basin_size += 1
                next_points = []
                for difference in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                    next_point = tuple(
                        [a + b for a, b in zip((x, y), difference)])
                    if all(k >= 0 for k in next_point) and\
                            next_point[0] < len(heightmap) and\
                            next_point[1] < len(heightmap[next_point[0]]) and\
                            not visited[next_point[0]][next_point[1]]:
                        next_points.append(next_point)
                        visited[next_point[0]][next_point[1]] = True
                points_to_visit.extend(next_points)

            next_size = basin_size
            for k in range(3):
                if next_size > largest_basins[k]:
                    temp = largest_basins[k]
                    largest_basins[k] = next_size
                    next_size = temp
    return largest_basins[0] * largest_basins[1] * largest_basins[2]


def get_data():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
