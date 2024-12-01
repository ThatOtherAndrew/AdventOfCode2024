def main():
    with open('input.txt') as file:
        data = [list(map(int, line.split())) for line in file]
    sorted_data = zip(sorted([row[0] for row in data]), sorted([row[1] for row in data]))
    print(sum(abs(row[0] - row[1]) for row in sorted_data))


if __name__ == '__main__':
    main()
