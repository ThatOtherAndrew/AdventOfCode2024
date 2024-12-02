def main():
    with open('input.txt') as file:
        data = [list(map(int, line.split())) for line in file]

    safe = 0
    for line in data:
        if line in (sorted(line), sorted(line, reverse=True)) and all(1 <= abs(line[i + 1] - line[i]) <= 3 for i in range(len(line) - 1)):
            safe += 1

    print(safe)


if __name__ == '__main__':
    main()
