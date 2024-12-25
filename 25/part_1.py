from itertools import product


def main():
    locks = []
    keys = []

    with open('input.txt') as file:
        for schematic in file.read().split('\n\n'):
            lines = [line.strip() for line in schematic.splitlines()]
            heights = [-1 for _ in lines[0]]
            for line in lines:
                for i, char in enumerate(line):
                    heights[i] += char == '#'
            (locks if schematic.startswith('#') else keys).append(heights)

    print(sum(
        all(height <= 5 for height in map(sum, zip(lock, key)))
        for lock, key in product(locks, keys)
    ))


if __name__ == '__main__':
    main()
