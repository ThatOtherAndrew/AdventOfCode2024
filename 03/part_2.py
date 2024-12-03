import re


def main():
    with open('input.txt') as file:
        data = file.read().strip()

    total = 0
    dos = {match.start() for match in re.finditer(r'do\(\)', data)} | {0}
    donts = {match.start() for match in re.finditer(r"don't\(\)", data)}

    for mul in re.finditer(r'mul\((\d+),(\d+)\)', data):
        def lt_pos(num: int) -> bool:
            return num < mul.start()

        x, y = map(int, mul.group(1, 2))
        if max(filter(lt_pos, dos)) > max(filter(lt_pos, donts), default=-1):
            total += x * y

    print(total)


if __name__ == '__main__':
    main()
