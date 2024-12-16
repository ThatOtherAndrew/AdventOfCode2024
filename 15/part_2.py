from itertools import chain

import numpy as np

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}
REMAP = {
    '#': '##',
    'O': '[]',
    '.': '..',
    '@': '@.',
}


def main():
    with open('input.txt') as file:
        raw_map, instructions = file.read().split('\n\n')
        warehouse = np.array([list(chain(*[REMAP[char] for char in line])) for line in raw_map.splitlines()])
        instructions = instructions.replace('\n', '')

    position = np.argwhere(warehouse == '@')[0]
    warehouse[*position] = '.'

    for i, instruction in enumerate(instructions):
        direction = DIRECTIONS[instruction]
        pushed_boxes = []
        cursors = [position + direction]
        blocked = False

        while cursors:
            new_cursors = []
            for cursor in cursors:
                char = warehouse[*cursor]
                if char == '#':
                    blocked = True
                    break
                elif char in '[]':
                    if char == ']':
                        pushed_boxes.append(cursor - (0, 1))
                    else:
                        pushed_boxes.append(cursor)
                    # noinspection PyTypeChecker
                    new_cursors.append(cursor + direction)
                    if direction[0] != 0:
                        new_cursors.append(cursor + direction + (0, 1 if char == '[' else -1))

            if blocked:
                break
            cursors = new_cursors

        if not blocked:
            for box_pos in pushed_boxes:
                warehouse[box_pos[0], box_pos[1]:box_pos[1] + 2] = '.'
            for box_pos in pushed_boxes:
                new_pos = box_pos + direction
                warehouse[new_pos[0], new_pos[1]:new_pos[1] + 2] = list('[]')
            position += direction

    print(sum(100 * box[0] + box[1] for box in np.argwhere(warehouse == '[')))


if __name__ == '__main__':
    main()
