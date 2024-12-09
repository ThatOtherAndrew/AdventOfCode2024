from itertools import dropwhile


def main():
    with open('input.txt') as file:
        disk_map = list(map(int, file.read().strip()))

    # This is an oh so naive implementation and part 2 is definitely an optimisation problem
    # I'm scared already
    disk = []
    for i, size in enumerate(disk_map):
        id_num = None if i % 2 else i // 2
        disk += [id_num] * size

    while None in dropwhile(lambda block: block is None, reversed(disk)):
        cursor = len(disk) - 1
        while (value := disk[cursor]) is None:
            cursor -= 1  # seek to last file block
        disk[cursor] = None

        cursor = 0
        while disk[cursor] is not None:
            cursor += 1  # seek to first empty space
        disk[cursor] = value

    print(sum(i * id_num for i, id_num in enumerate(disk) if id_num is not None))

if __name__ == '__main__':
    main()
