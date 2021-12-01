def main():
    with open("input.txt", 'r') as f:
        depths = [int(d) for d in f.readlines()]
        
    count = 0
    prev = depths[0]
    for d in depths[1:]:
        if d > prev:
            count += 1
        prev = d

    print(f"The number of measurements larger than the previous measurement is: {count}")

if __name__ == "__main__":
    main()
