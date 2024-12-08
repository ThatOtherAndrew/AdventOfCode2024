import itertools

import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        city_map = np.array([list(line.strip()) for line in file])
        antinodes = np.zeros_like(city_map, dtype=bool)

    for antenna in np.unique(city_map):
        if antenna == '.':
            continue

        positions = np.argwhere(city_map == antenna)
        for a, b in itertools.combinations(positions, 2):
            vector = (b - a)
            vector //= np.gcd(*vector)  # simplify x:y ratio
            pos = a.copy()
            while pos_in_map(pos - vector, city_map):
                pos -= vector
            while pos_in_map(pos, city_map):
                antinodes[*pos] = True
                pos += vector

    print(np.sum(antinodes))


if __name__ == '__main__':
    main()
