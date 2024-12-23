from itertools import combinations


def main():
    network = {}
    with open('input.txt') as file:
        for a, b in [line.strip().split('-') for line in file]:
            network.setdefault(a, []).append(b)
            network.setdefault(b, []).append(a)

    triples = set()
    for node, connections in network.items():
        for a, b in combinations(connections, 2):
            if a in network[b]:
                triples.add(tuple(sorted([node, a, b])))

    print(sum(any(node.startswith('t') for node in triple) for triple in triples))


if __name__ == '__main__':
    main()
