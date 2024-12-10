import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        trail_map = np.array([[10 if char == '.' else int(char) for char in line.strip()] for line in file])

    score = 0
    for trailhead in np.argwhere(trail_map == 0):
        reachable_nines = set()
        cursors = {tuple(trailhead): trailhead}
        while cursors:
            new_cursors = {}
            for cursor in cursors.values():
                for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    if not pos_in_map(next_pos := cursor + direction, trail_map):
                        continue
                    elif (next_val := trail_map[*next_pos]) == trail_map[*cursor] + 1:
                        if next_val == 9:
                            reachable_nines.add(tuple(next_pos))
                        else:
                            new_cursors[tuple(next_pos)] = next_pos
            cursors = new_cursors
        score += len(reachable_nines)

    print(score)


if __name__ == '__main__':
    main()
