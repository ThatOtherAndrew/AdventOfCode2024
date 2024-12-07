import itertools
from math import log

from tqdm import tqdm


def main():
    with open('input.txt') as file:
        equations = []
        for line in file:
            raw_target, raw_operands = line.split(': ')
            equations.append((int(raw_target), list(map(int, raw_operands.split()))))

    total = 0
    for target, operands in tqdm(equations):
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
                total += calculation
                break

    print(total)

if __name__ == '__main__':
    main()
