from tqdm import tqdm


def main():
    with open('input.txt') as file:
        disk_map = list(map(int, file.read().strip()))

    disk = []
    for i, size in enumerate(disk_map):
        id_num = None if i % 2 else i // 2
        disk += [id_num] * size

    for i in tqdm(range(len(disk) - 1, -1, -1)):
        if disk[i] is None:
            continue

        first_empty_index = disk.index(None)
        if first_empty_index > i:
            break  # we can end early once the first empty space is to the right of the current block
        disk[first_empty_index] = disk[i]
        disk[i] = None

    print(sum(i * id_num for i, id_num in enumerate(disk) if id_num is not None))

if __name__ == '__main__':
    main()
