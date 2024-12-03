import re


def main():
    with open('input.txt') as file:
        data = file.read().strip()

    total = 0
    for mul in re.finditer(r'mul\((\d+),(\d+)\)', data):
        x, y = map(int, mul.group(1, 2))
        total += x * y

    print(total)


if __name__ == '__main__':
    main()
