import numpy as np

# noinspection PyTypeChecker
# ^ because PyCharm is dumb
XMAS_MASKS: list[np.ndarray[str]] = list(map(np.array, (
    [
        ['X', 'M', 'A', 'S']
    ],
    [
        ['X'],
        ['M'],
        ['A'],
        ['S'],
    ],
    [
        ['X', '.', '.', '.'],
        ['.', 'M', '.', '.'],
        ['.', '.', 'A', '.'],
        ['.', '.', '.', 'S'],
    ],
    [
        ['.', '.', '.', 'X'],
        ['.', '.', 'M', '.'],
        ['.', 'A', '.', '.'],
        ['S', '.', '.', '.'],
    ],
)))
# noinspection PyTypeChecker
# Mirror the above masks
XMAS_MASKS += list(map(np.flip, XMAS_MASKS))


def main():
    with open('input.txt') as file:
        wordsearch = np.array([list(line.strip()) for line in file])

    count = 0
    for mask in XMAS_MASKS:
        for y in range(wordsearch.shape[0] - mask.shape[0] + 1):
            for x in range(wordsearch.shape[1] - mask.shape[1] + 1):
                pos = slice(y, y+mask.shape[0]), slice(x, x+mask.shape[1])
                cmp = wordsearch[pos]
                if np.all((mask == cmp) | (mask == '.')):
                    count += 1


    print(count)


if __name__ == '__main__':
    main()
