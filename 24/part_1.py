from graphlib import TopologicalSorter


def main():
    circuit = {}
    graph = TopologicalSorter()

    with open('input.txt') as file:
        initial, gates = file.read().split('\n\n')
        for line in initial.splitlines():
            wire, value = line.split(': ')
            circuit[wire] = int(value)
        for line in gates.splitlines():
            in_a, gate, in_b, _, out = line.split()
            circuit[out] = (gate, in_a, in_b)
            graph.add(out, in_a, in_b)

    for wire in graph.static_order():
        match circuit[wire]:
            case ['AND', a, b]:
                circuit[wire] = circuit[a] & circuit[b]
            case ['OR', a, b]:
                circuit[wire] = circuit[a] | circuit[b]
            case ['XOR', a, b]:
                circuit[wire] = circuit[a] ^ circuit[b]

    bits = ''.join(str(value) for wire, value in sorted(circuit.items()) if wire.startswith('z'))
    print(int(bits[::-1], base=2))


if __name__ == '__main__':
    main()
