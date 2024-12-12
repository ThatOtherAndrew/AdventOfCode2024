import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def count_sides(tiles: set[tuple[int, int]]) -> int:  # in retrospect it would've been neater to count corners
    sides = 0

    for _ in range(4):
        prev_pos = (None, None)
        for pos in map(np.array, sorted(tiles)):
            if tuple(pos - (1, 0)) not in tiles:  # if position above isn't a tile (there is an upper edge)
                if np.any(prev_pos != pos - (0, 1)):  # if previous position with an upper edge isn't to the left
                    sides += 1
                prev_pos = tuple(pos)
        tiles = {(-tile[1], tile[0]) for tile in tiles}  # rotate ccw 90 degrees

    return sides


def main():
    with open('input.txt') as file:
        garden = np.array([list(line.strip()) for line in file])
        checked = np.zeros_like(garden, dtype=bool)

    price = 0

    while not np.all(checked):
        tiles = set()
        cursors = [np.argwhere(~checked)[0]]
        plant_type = garden[*cursors[0]]

        while cursors:
            new_cursors = set()
            for cursor in cursors:
                checked[*cursor] = True
                tiles.add(tuple(cursor))
                adjacent = {
                    tuple(cursor + direction)
                    for direction in ((0, 1), (1, 0), (0, -1), (-1, 0))
                    if pos_in_map(new_cursor := cursor + direction, garden) and garden[*new_cursor] == plant_type
                }
                new_cursors |= {new_cursor for new_cursor in adjacent if not checked[*new_cursor]}
            cursors = list(map(np.array, new_cursors))

        # noinspection PyTypeChecker
        price += len(tiles) * count_sides(tiles)

    print(price)


if __name__ == '__main__':
    main()
