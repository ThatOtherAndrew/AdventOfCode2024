import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        trail_map = np.array([[10 if char == '.' else int(char) for char in line.strip()] for line in file])

    ratings = np.zeros_like(trail_map)
    cursors = {}
    for trailhead in np.argwhere(trail_map == 0):
        cursors[tuple(trailhead)] = trailhead
        ratings[*trailhead] = 1

    while cursors:
        new_cursors = {}
        for cursor in cursors.values():
            for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if not pos_in_map(next_pos := cursor + direction, trail_map):
                    continue
                elif trail_map[*next_pos] == trail_map[*cursor] + 1:
                    ratings[*next_pos] += ratings[*cursor]
                    new_cursors[tuple(next_pos)] = next_pos
        cursors = new_cursors

    print(np.sum(ratings[trail_map == 9]))


if __name__ == '__main__':
    main()
