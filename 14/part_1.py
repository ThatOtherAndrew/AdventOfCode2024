import numpy as np


ITERATIONS = 100
WIDTH = 101
HEIGHT = 103


def main():
    with open('input.txt') as file:
        robots = []
        for line in file:
            raw_p, raw_v = line.split()
            pos = np.array(list(map(int, raw_p.removeprefix('p=').split(','))))
            vel = np.array(list(map(int, raw_v.removeprefix('v=').split(','))))
            robots.append([pos, vel])

    quadrants = [0, 0, 0, 0]
    for robot in robots:
        robot[0] = (robot[0] + (robot[1] * ITERATIONS)) % (WIDTH, HEIGHT)
        for i, (a, b) in enumerate(((1, 1), (1, -1), (-1, 1), (-1, -1))):
            if a * robot[0][0] < a * (WIDTH // 2) and b * robot[0][1] < b * (HEIGHT // 2):
                quadrants[i] += 1


    print(np.prod(quadrants))


if __name__ == '__main__':
    main()
