def part1():
    data = get_data()
    outputs = [d[1] for d in data]

    count = 0
    for entry in outputs:
        for digit in entry:
            if len(digit) in (2, 4, 3, 7):
                count += 1

    return count


def part2():
    # Get data and parse into the form we need it
    data = get_data()
    parsed_data = []
    for line in data:
        new_line = ([], [])
        for item in line[0]:
            inner_set = set()
            for char in item:
                inner_set.add(char)
            new_line[0].append(inner_set)
        for item in line[1]:
            inner_set = set()
            for char in item:
                inner_set.add(char)
            new_line[1].append(inner_set)
        parsed_data.append(new_line)

    original_segments = [
        {"a", "b", "c", "e", "f", "g"}, {"c", "f"}, {"a", "c", "d", "e", "g"}, {
            "a", "c", "d", "f", "g"}, {"b", "c", "d", "f"},
        {"a", "b", "d", "f", "g"}, {"a", "b", "d", "e", "f", "g"}, {
            "a", "c", "f"}, {"a", "b", "c", "d", "e", "f", "g"}, {"a", "b", "c", "d", "f", "g"},
    ]

    final_sum = 0
    for line in parsed_data:

        digit_segments = {}
        segment_mixup = {}
        possible_segs235 = []
        possible_segs069 = []
        for digit in line[0]:
            num_segments_in_digit = len(digit)
            if num_segments_in_digit == 2:
                digit_segments[1] = digit
            elif num_segments_in_digit == 4:
                digit_segments[4] = digit
            elif num_segments_in_digit == 3:
                digit_segments[7] = digit
            elif num_segments_in_digit == 7:
                digit_segments[8] = digit
            elif num_segments_in_digit == 5:
                possible_segs235.append(digit)
            elif num_segments_in_digit == 6:
                possible_segs069.append(digit)

        segment_mixup['a'] = digit_segments[7].difference(
            digit_segments[1])

        for digit in possible_segs235:
            difference = digit.difference(digit_segments[4])
            if len(difference) == 2:
                segment_mixup['g'] = difference.difference(
                    segment_mixup['a'])
                break
        for digit in possible_segs235:
            difference = digit.difference(digit_segments[4])
            if len(difference) == 3:
                segment_mixup['e'] = difference.difference(
                    segment_mixup['a'].union(segment_mixup['g']))
                segment_mixup['f'] = digit_segments[1].difference(
                    digit)
                segment_mixup['c'] = digit_segments[1].difference(
                    segment_mixup['f'])
                digit_segments[2] = digit
                segment_mixup['d'] = digit_segments[2].difference(
                    segment_mixup['a'].union(segment_mixup['c']).union(
                        segment_mixup['e'].union(segment_mixup['g'])))
                segment_mixup['b'] = digit_segments[8].difference(
                    digit_segments[2]).difference(segment_mixup['f'])
                break
        true_number = 0
        for i, digit in enumerate(line[1]):
            true_segments = set()
            for segment in digit:
                for true_seg, current in segment_mixup.items():
                    if segment in current:
                        true_segments.update(true_seg)
            for j, segment in enumerate(original_segments):
                if true_segments == segment:
                    true_digit = j
                    break
            true_number += (10**(3-i)) * true_digit

        final_sum += true_number

    return final_sum


def get_data():
    with open("input.txt", "r") as f:
        return [(line[0].split(), line[1].split()) for line in
                [line.split("|") for line in f.readlines()]]


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
