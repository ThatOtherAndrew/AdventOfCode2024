from collections import Counter


def main():
    with open('input.txt') as file:
        stones = Counter([int(num) for num in file.read().split()])

    # oh that really wasn't too bad
    for _ in range(75):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(s := str(stone)) % 2 == 0:
                new_stones[int(s[:len(s) // 2])] += count
                new_stones[int(s[len(s) // 2:])] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones

    print(sum(stones.values()))


if __name__ == '__main__':
    main()
