from graphlib import TopologicalSorter


def main():
    with open('input.txt') as file:
        raw_rules, raw_updates = file.read().split('\n\n')
        rules = [tuple(map(int, line.split('|'))) for line in raw_rules.splitlines()]
        updates = [list(map(int, line.split(','))) for line in raw_updates.splitlines()]

    total = 0
    for update in updates:
        graph = TopologicalSorter()
        for before, after in rules:
            if before in update and after in update:
                graph.add(after, before)

        order = list(graph.static_order())
        indexes = [order.index(page) for page in update]

        if indexes == sorted(indexes):
            total += update[len(update) // 2]

    print(total)


if __name__ == '__main__':
    main()
