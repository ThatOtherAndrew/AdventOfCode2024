def mutate(number: int) -> int:
    number = (number ^ (number * 64)) % 16777216
    number = (number ^ (number // 32)) % 16777216
    return (number ^ (number * 2048)) % 16777216


def main():
    with open('input.txt') as file:
        secret_numbers = list(map(int, file.readlines()))

    for _ in range(2000):
        secret_numbers = list(map(mutate, secret_numbers))

    print(sum(secret_numbers))


if __name__ == '__main__':
    main()
