import numpy as np

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}


def main():
    with open('input.txt') as file:
        raw_map, instructions = file.read().split('\n\n')
        warehouse = np.array([list(line) for line in raw_map.splitlines()])
        instructions = instructions.replace('\n', '')

    position = np.argwhere(warehouse == '@')[0]
    warehouse[*position] = '.'

    for i, instruction in enumerate(instructions):
        direction = DIRECTIONS[instruction]
        target = position + direction
        while warehouse[*target] == 'O':
            target += direction

        if warehouse[*target] == '.':
            position += direction
            warehouse[*position] = '.'
            box_pos = np.copy(position + direction)
            while np.any(box_pos != target + direction):
                warehouse[*box_pos] = 'O'
                box_pos += direction

    print(sum(100 * box[0] + box[1] for box in np.argwhere(warehouse == 'O')))


if __name__ == '__main__':
    main()
