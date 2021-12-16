import sys


def part1():
    data = get_data()
    template = data[0].strip()

    insertion_rules = [line.strip().split(" -> ") for line in data[2:]]
    for _ in range(10):
        new_template = [template[0]]
        for i in range(len(template) - 1):
            pair = template[i:i+2]
            for rule in insertion_rules:
                if pair == rule[0]:
                    new_template.extend([rule[1], pair[1]])
                    break
        template = "".join(new_template)

    d = {}
    for element in template:
        if not d.get(element):
            d[element] = 1
        else:
            d[element] += 1
    freq_max = 0
    freq_min = sys.maxsize
    for k, v in d.items():
        if v > freq_max:
            freq_max = v
        if v < freq_min:
            freq_min = v

    return freq_max - freq_min


def part2():
    data = get_data()
    template = data[0].strip()

    insertion_rules = {pair: insert for pair, insert in [
        line.strip().split(" -> ") for line in data[2:]]}
    pairs = list(insertion_rules.keys())
    initial_pairs = [template[i:i+2] for i in range(len(template) - 1)]
    element_counts = {elt: 0 for elt in template}
    pair_counts = {key: 0 for key in insertion_rules}

    for elt in template:
        element_counts[elt] += 1

    for pair in initial_pairs:
        pair_counts[pair] += 1

    for _ in range(40):
        new_pair_counts = {pair: 0 for pair in pairs}
        for pair in pairs:
            count = pair_counts[pair]
            if count > 0:
                insertion = insertion_rules[pair]
                new_pair_counts[f"{pair[0]}{insertion}"] += count
                new_pair_counts[f"{insertion}{pair[1]}"] += count
                if element_counts.get(insertion) != None:
                    element_counts[insertion] += count
                else:
                    element_counts[insertion] = count
        pair_counts = new_pair_counts

    freq_max = 0
    freq_min = sys.maxsize
    for k, v in element_counts.items():
        if v > freq_max:
            freq_max = v
        if v < freq_min:
            freq_min = v

    return freq_max - freq_min


def get_data():
    with open("input.txt", "r") as f:
        return f.readlines()


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()
