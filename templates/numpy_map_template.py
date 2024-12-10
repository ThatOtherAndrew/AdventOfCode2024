import numpy as np


def pos_in_map(position: np.ndarray[int], map_array: np.ndarray):
    return all(position[axis] in range(size) for axis, size in enumerate(map_array.shape))


def main():
    with open('input.txt') as file:
        input_map = np.array([list(line.strip()) for line in file])

    print(input_map)


if __name__ == '__main__':
    main()
