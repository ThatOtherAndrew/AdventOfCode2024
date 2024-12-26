from functools import cache


def main():
    with open('input.txt') as file:
        towels = set(file.readline().strip().split(', '))
        designs = file.read().split()

    @cache
    def count_arrangements(design: str) -> int:
        if not design:
            return 1
        return sum(
            count_arrangements(design.removeprefix(towel))
            for towel in towels
            if design.startswith(towel)
        )

    print(sum(map(count_arrangements, designs)))


if __name__ == '__main__':
    main()
