from collections import deque

from tqdm import tqdm

MAX_CHANGES = 2000
DIFF_WINDOW = 4


def changes(seed: int):
    last_num = seed % 10
    for _ in range(MAX_CHANGES):
        seed = (seed ^ (seed * 64)) % 16777216
        seed = (seed ^ (seed // 32)) % 16777216
        seed = (seed ^ (seed * 2048)) % 16777216
        new_num = seed % 10
        yield new_num, new_num - last_num
        last_num = new_num


def main():
    with open('input.txt') as file:
        all_prices = []
        for seed in map(int, file.readlines()):
            price_map = {}
            generator = changes(seed)
            window = deque((next(generator)[1] for _ in range(DIFF_WINDOW - 1)), maxlen=DIFF_WINDOW)
            while (new := next(generator, None)) is not None:
                window.append(new[1])
                price_map.setdefault(tuple(window), new[0])
            all_prices.append(price_map)

    print(max(
        sum(prices.get(sequence, 0) for prices in all_prices)
        for sequence in tqdm(set().union(*(prices.keys() for prices in all_prices)))
    ))


if __name__ == '__main__':
    main()
