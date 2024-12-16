import numpy as np
from PIL import Image

WIDTH = 101
HEIGHT = 103


def render_frame(positions: list[np.ndarray]) -> Image.Image:
    frame_data = np.zeros((HEIGHT, WIDTH), dtype=bool)
    for position in positions:
        frame_data[position[1], position[0]] = True
    return Image.fromarray(frame_data)


def main():
    with open('input.txt') as file:
        positions = []
        velocities = []
        for line in file:
            raw_p, raw_v = line.split()
            positions.append(np.array(list(map(int, raw_p.removeprefix('p=').split(',')))))
            velocities.append(np.array(list(map(int, raw_v.removeprefix('v=').split(',')))))

    frames = [render_frame(positions)]
    while len(set(map(tuple, positions))) < len(positions):
        for position, velocity in zip(positions, velocities):
            position += velocity
            position %= (WIDTH, HEIGHT)
        frames.append(render_frame(positions))

    frames[0].save('out.gif', save_all=True, append_images=frames[1:], loop=0)
    print(len(frames) - 1)


if __name__ == '__main__':
    main()
