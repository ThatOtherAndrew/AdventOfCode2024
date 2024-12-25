import numpy as np
from tqdm import tqdm

MAX_COORDINATE = 70
FALL = 1024


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        corruptions = [tuple(map(int, line.split(',')))[::-1] for line in file]
    corruptions_grid = np.zeros((MAX_COORDINATE + 1, MAX_COORDINATE + 1), dtype=bool)
    for corruption in corruptions[:FALL]:
        corruptions_grid[*corruption] = True

    # This can definitely be done in a cleverer way using a binary search. However, I'm lazy!
    for corruption in tqdm(corruptions[FALL:]):
        cursors = {(0, 0)}
        steps = 0
        corruptions_grid[*corruption] = True
        grid = corruptions_grid.copy()

        while cursors:
            if (MAX_COORDINATE, MAX_COORDINATE) in cursors:
                break
            new_cursors = set()

            for cursor in cursors:
                grid[*cursor] = True
                for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    next_pos = np.array(cursor) + direction
                    if pos_in_map(next_pos, grid) and not grid[*next_pos]:
                        new_cursors.add(tuple(next_pos))

            cursors = new_cursors
            steps += 1

        if not cursors:
            print(f'{corruption[1]},{corruption[0]}')
            break


if __name__ == '__main__':
    main()
