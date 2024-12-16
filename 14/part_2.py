import numpy as np

WIDTH = 101
HEIGHT = 103


def main():
    with open('input.txt') as file:
        positions = []
        velocities = []
        for line in file:
            raw_p, raw_v = line.split()
            positions.append(np.array(list(map(int, raw_p.removeprefix('p=').split(',')))))
            velocities.append(np.array(list(map(int, raw_v.removeprefix('v=').split(',')))))

    iterations = 0
    while len(set(map(tuple, positions))) < len(positions):
        for position, velocity in zip(positions, velocities):
            position += velocity
            position %= (WIDTH, HEIGHT)
        iterations += 1

    picture = np.zeros((HEIGHT, WIDTH), dtype=bool)
    for position in positions:
        picture[position[1], position[0]] = True
    print(iterations)


if __name__ == '__main__':
    main()
