from dataclasses import dataclass, field
from itertools import pairwise

import numpy as np
from tqdm import tqdm


@dataclass(order=True)
class Block:
    id: int = field(compare=False)
    pos: int
    size: int = field(compare=False)


def visualise(blocks: list[Block], length: int) -> str:
    disk = np.full(length, '.', dtype=str)
    for blk in blocks:
        disk[blk.pos:blk.pos + blk.size] = str(blk.id)
    return ''.join(disk)


def main():
    # Use on sample inputs only! Hard-coded example below
    disk_map = list(map(int, '2333133121414131402'))

    blocks = []
    pos = 0
    data_length = 0
    for i, size in enumerate(disk_map):
        if i % 2 == 0:
            blocks.append(Block(i // 2, pos, size))
            data_length += size
        pos += size

    print(visualise(blocks, pos))

    for block in sorted(blocks, key=lambda blk: blk.id, reverse=True):
        for left, right in pairwise(blocks):
            if left is block:
                break  # avoid moving block right

            space_start = left.pos + left.size
            if (right.pos - space_start) >= block.size:
                block.pos = space_start
                blocks.sort()
                break

        print(f'{visualise(blocks, pos)} (moved block {block.id})')

    print(sum(block.id * sum(i for i in range(block.pos, block.pos + block.size)) for block in blocks))


if __name__ == '__main__':
    main()
