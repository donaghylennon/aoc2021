def main():
    with open("input.txt", 'r') as f:
        depths = [int(d) for d in f.readlines()]

    count = 0
    prev_sum = sum(depths[0:3])
    for i in range(1, len(depths) - 2):
        next_sum = sum(depths[i:i+3])
        if next_sum > prev_sum:
            count += 1
        prev_sum = next_sum

    print(f"The number of times the sliding window sum is greater than the previous is: {count}")


if __name__ == "__main__":
    main()
