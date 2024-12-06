from concurrent.futures.process import ProcessPoolExecutor
from itertools import repeat

import numpy as np
from tqdm import tqdm


def pos_in_map(position: np.ndarray, map_array: np.ndarray) -> bool:
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def is_looping(lab_map: np.ndarray, new_obstacle_pos: tuple[int, int]) -> bool:
    if lab_map[new_obstacle_pos] != '.':
        return False

    new_map = lab_map.copy()
    new_map[new_obstacle_pos] = '#'
    position: np.ndarray = np.argwhere(new_map == '^')[0]
    direction = (-1, 0)
    prev_states = set()

    while True:
        while pos_in_map(next_pos := position + direction, new_map) and new_map[*next_pos] != '#':
            position = next_pos
        if not pos_in_map(next_pos, new_map):
            return False

        direction = (direction[1], -direction[0])
        if (*position, *direction) in prev_states:
            return True
        prev_states.add((*position, *direction))


def main():
    with open('input.txt') as file:
        lab_map = np.array([list(line.strip()) for line in file])

    # This is incredibly brute-forcey but I can't think of a straightforward more efficient way.
    with ProcessPoolExecutor() as executor:
        loops = tqdm(executor.map(is_looping, repeat(lab_map), np.ndindex(lab_map.shape)), total=lab_map.size)
        print(sum(loops))

    # count = 0
    # for index in tqdm(np.ndindex(lab_map.shape), total=lab_map.size):
    #     if is_looping(lab_map, index):
    #         count += 1
    # print(count)


if __name__ == '__main__':
    main()
