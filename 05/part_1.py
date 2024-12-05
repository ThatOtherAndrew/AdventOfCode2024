def main():
    with open('input.txt') as file:
        raw_rules, raw_updates = file.read().split('\n\n')
        rules = [tuple(map(int, line.split('|'))) for line in raw_rules.splitlines()]
        updates = [list(map(int, line.split(','))) for line in raw_updates.splitlines()]

    total = 0
    for update in updates:
        if all(
            update.index(before) < update.index(after)
            for before, after in rules
            if before in update and after in update
        ):
            total += update[len(update) // 2]

    print(total)


if __name__ == '__main__':
    main()
