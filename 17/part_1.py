def main():
    with open('input.txt') as file:
        register_input, program_input = file.read().split('\n\n')
        memory = [int(line.split()[-1]) for line in register_input.splitlines()]
        program = list(map(int, program_input.removeprefix('Program: ').split(',')))

    def combo(combo_operand: int):
        if combo_operand in range(4):
            return combo_operand
        elif combo_operand in range(4, 7):
            return memory[combo_operand - 4]
        else:
            raise NotImplementedError

    pointer = 0
    output = []

    while pointer in range(len(program) - 1):
        instruction, operand = program[pointer:pointer + 2]

        if instruction == 0:    # adv
            memory[0] = int(memory[0] / 2 ** combo(operand))
        elif instruction == 1:  # bxl
            memory[1] ^= operand
        elif instruction == 2:  # bst
            memory[1] = combo(operand) % 8
        elif instruction == 3:  # jnz
            if memory[0]:
                pointer = operand
                continue
        elif instruction == 4:  # bxc
            memory[1] = memory[1] ^ memory[2]
        elif instruction == 5:  # out
            output.append(combo(operand) % 8)
        elif instruction == 6:  # bdv
            memory[1] = int(memory[0] / 2 ** combo(operand))
        elif instruction == 7:  # cdv
            memory[2] = int(memory[0] / 2 ** combo(operand))

        pointer += 2

    print(*output, sep=',')


if __name__ == '__main__':
    main()
