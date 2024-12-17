import re

import numpy as np


def main():
    with open('input.txt') as file:
        machines = file.read().split('\n\n')

    tokens = 0
    for machine in machines:
        ax, ay, bx, by, tx, ty = map(int, re.findall(r'\d+', machine))
        unscaled = np.matmul([[by, -bx], [-ay, ax]], np.array([tx, ty]) + int(1e13))
        determinant = ax * by - ay * bx
        if np.all(unscaled % determinant == 0):
            tokens += np.sum(unscaled // determinant * (3, 1))

    print(tokens)


if __name__ == '__main__':
    main()
