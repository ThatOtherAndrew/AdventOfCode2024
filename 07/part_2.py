import itertools
from concurrent.futures.process import ProcessPoolExecutor
from math import log

from tqdm import tqdm


def test_equation(target: int, operands: list[int]) -> int:
    for operators in itertools.product('+*|', repeat=len(operands) - 1):
        calculation = operands[0]
        for op, num in zip(operators, operands[1:]):
            if op == '+':
                calculation += num
            elif op == '*':
                calculation *= num
            else:
                calculation = calculation * (10 ** int(log(num, 10) + 1)) + num

        if calculation == target:
            return target

    return 0


def main():
    with open('input.txt') as file:
        equations = []
        for line in file:
            raw_target, raw_operands = line.split(': ')
            equations.append((int(raw_target), list(map(int, raw_operands.split()))))

    with ProcessPoolExecutor() as executor:
        tested_equations = list(tqdm(executor.map(test_equation, *zip(*equations)), total=len(equations)))

    print(sum(tested_equations))

if __name__ == '__main__':
    main()
