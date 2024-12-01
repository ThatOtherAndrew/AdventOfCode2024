def main():
    with open('input.txt') as file:
        data = [list(map(int, line.split())) for line in file]
    left = [row[0] for row in data]
    right = [row[1] for row in data]
    total = 0
    for num in left:
        total += right.count(num) * num

    print(total)


if __name__ == '__main__':
    main()
