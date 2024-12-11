def main():
    with open('input.txt') as file:
        stones = [int(num) for num in file.read().split()]

    # oh no, I can feel the part 2 optimisation problem encroaching already
    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(s := str(stone)) % 2 == 0:
                new_stones.extend(map(int, (s[:len(s) // 2], s[len(s) // 2:])))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))


if __name__ == '__main__':
    main()
