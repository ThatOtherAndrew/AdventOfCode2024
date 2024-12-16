import numpy as np

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

def visualise(warehouse: np.ndarray, position: np.ndarray, instructions: str, index: int) -> str:
    warehouse = np.copy(warehouse)
    warehouse[*position] = '@'
    string = ''
    instruction_line = ''
    if index < len(instructions):
        instruction_line = f'\x1b[1;36m{instructions[index+1]}\x1b[0;34m{instructions[index+2:index+122]}\x1b[0m'

    for i, line in enumerate(warehouse):
        for char in line:
            style = {
                '#': '2;7;37',
                'O': '33',
                '.': '2;37',
                '@': '1;35',
            }[char]
            string += f'\x1b[0;{style}m{char}'
        string += '\x1b[0m'

        if i == 0:
            string += f'  {instruction_line}'
        elif i == 1 and index < len(instructions):
            vector = DIRECTIONS[instructions[index]]
            string += f'  \x1b[2;36m({vector[0]:>2}, {vector[1]:>2})\x1b[0m'
        string += '\n'

    return string


def main():
    with open('input.txt') as file:
        raw_map, instructions = file.read().split('\n\n')
        warehouse = np.array([list(line) for line in raw_map.splitlines()])
        instructions = instructions.replace('\n', '')

    position = np.argwhere(warehouse == '@')[0]
    warehouse[*position] = '.'
    print('\x1b[H\x1b[2J' + visualise(warehouse, position, instructions, -1), end='')
    #     ^^^^^^^^^^^^^^^  move cursor to top left and clear

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

        print('\x1b[H' + visualise(warehouse, position, instructions + ' ', i), end='')
        __import__('time').sleep(0.05)

    print(sum(100 * box[0] + box[1] for box in np.argwhere(warehouse == 'O')))


if __name__ == '__main__':
    main()
