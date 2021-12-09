import typing


class Board:
    won = False

    def __init__(self, rows):
        self.rows = rows
        self.markers = {
            i: False
            for row in rows
            for i in row
        }

    def mark_and_check(self, number):
        had_number = False
        for i, row in enumerate(self.rows):
            for j, square in enumerate(row):
                if square == number:
                    self.markers[number] = True
                    had_number = True
                    break
            if had_number:
                break

        # Check if board wins
        if had_number:
            win = True
            for square in self.rows[i]:
                if not self.markers[square]:
                    win = False
                    break
            if not win:
                win = True
                for square in [row[j] for row in self.rows]:
                    if not self.markers[square]:
                        win = False
                        break
            self.won = win
            return win
        else:
            return False

    def sum_unmarked(self):
        sum = 0
        for row in self.rows:
            for square in row:
                if not self.markers[square]:
                    sum += square
        return sum


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def part1():
    data = get_data()
    numbers = [int(i) for i in data[0].split(",")]

    boards = []
    rows = []
    num_rows = 0
    for line in data[2:]:
        if line == "\n":
            continue
        rows.append([int(i) for i in line.split()])
        num_rows += 1
        if num_rows == 5:
            boards.append(Board(rows))
            rows = []
            num_rows = 0

    for number in numbers:
        for board in boards:
            if board.mark_and_check(number):
                return board.sum_unmarked() * number


def part2():
    data = get_data()
    numbers = [int(i) for i in data[0].split(",")]

    boards = []
    rows = []
    num_rows = 0
    for line in data[2:]:
        if line == "\n":
            continue
        rows.append([int(i) for i in line.split()])
        num_rows += 1
        if num_rows == 5:
            boards.append(Board(rows))
            rows = []
            num_rows = 0

    num_boards_won = 0
    for number in numbers:
        for board in boards:
            if not board.won and board.mark_and_check(number):
                num_boards_won += 1
                if num_boards_won == len(boards):
                    return board.sum_unmarked() * number


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
