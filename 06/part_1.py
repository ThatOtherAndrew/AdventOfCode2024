import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        lab_map = np.array([list(line.strip()) for line in file])
        walked = np.zeros_like(lab_map, dtype=bool)

    position = np.argwhere(lab_map == '^')[0]
    direction = (-1, 0)
    while pos_in_map(position, lab_map):
        walked[*position] = True
        next_pos = position + direction
        if pos_in_map(next_pos, lab_map) and lab_map[*next_pos] == '#':
            # turn right
            direction = (direction[1], -direction[0])
        position += direction

    print(np.sum(walked))


if __name__ == '__main__':
    main()
