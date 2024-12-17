import re

import numpy as np


# noinspection PyTypeChecker
def main():
    with open('input.txt') as file:
        machines = file.read().split('\n\n')

    tokens = 0
    for machine in machines:
        ax, ay, bx, by, tx, ty = map(int, re.findall(r'\d+', machine))
        solution = np.linalg.solve([[ax, bx], [ay, by]], [tx, ty])
        if np.isclose(solution, np.rint(solution)).all():
            tokens += round(3 * solution[0] + solution[1])

    print(tokens)


if __name__ == '__main__':
    main()
