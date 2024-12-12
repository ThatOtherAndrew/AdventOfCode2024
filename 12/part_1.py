import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        garden = np.array([list(line.strip()) for line in file])
        checked = np.zeros_like(garden, dtype=bool)

    price = 0

    while not np.all(checked):
        area = 0
        perimeter = 0
        cursors = [np.argwhere(~checked)[0]]
        plant_type = garden[*cursors[0]]

        while cursors:
            new_cursors = set()
            for cursor in cursors:
                checked[*cursor] = True
                area += 1
                adjacent = {
                    tuple(cursor + direction)
                    for direction in ((0, 1), (1, 0), (0, -1), (-1, 0))
                    if pos_in_map(new_cursor := cursor + direction, garden) and garden[*new_cursor] == plant_type
                }
                perimeter += 4 - len(adjacent)
                new_cursors |= {new_cursor for new_cursor in adjacent if not checked[*new_cursor]}
            cursors = list(map(np.array, new_cursors))

        price += area * perimeter

    print(price)


if __name__ == '__main__':
    main()
