def part1():
    data = get_data()

    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    opening_of = {')': '(', ']': '[', '}': '{', '>': '<'}
    total_score = 0
    for line in data:
        stack = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                stack.append(char)
            elif char in (')', ']', '}', '>'):
                if opening_of[char] != stack.pop():
                    total_score += scores[char]
                    break

    return total_score


def part2():
    data = get_data()

    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    opening_of = {')': '(', ']': '[', '}': '{', '>': '<'}
    closing_of = {'(': ')', '[': ']', '{': '}', '<': '>'}
    line_scores = []
    for line in data:
        stack = []
        corrupted = False
        for char in line:
            if char in ('(', '[', '{', '<'):
                stack.append(char)
            elif char in (')', ']', '}', '>'):
                if opening_of[char] != stack.pop():
                    corrupted = True
                    break
        if len(stack) > 0 and not corrupted:
            total_score = 0
            for char in stack[::-1]:
                total_score = total_score*5 + scores[closing_of[char]]
            line_scores.append(total_score)

    line_scores.sort()
    final_score = line_scores[len(line_scores) // 2]

    return final_score


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
