import argparse

neighbors = []
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        neighbors.append((i, j))
neighbors.remove((0, 0))


def main():
    steps = 0
    total_flashes = 0
    octopi, flashes = get_octopi()
    while total_flashes < 100:
        # octopi, flashes = iteration(octopi, flashes)
        total_flashes = iteration(octopi, flashes)
        steps += 1
    print(steps)
    # for row in octopi[1:-1]:
    #     print(row[1:-1])
    # print("\n" * 4)
    # for row in octopi:
    #     print(row)


def iteration(octopi, flashes):
    """
    increment all octopi by 1
    mark everything OVER a 9 in a parallel array as flash
    visit all octopi again, if didn't flash, count flashing neighbors and add this value
    """
    total_flashes = 0
    to_flash = []
    for r_idx, row in enumerate(octopi[1:-1], 1):
        for c_idx, col in enumerate(row[1:-1], 1):
            row[c_idx] += 1
            if row[c_idx] > 9:
                flashes[r_idx][c_idx] = 1
                total_flashes += 1
                to_flash.append((r_idx, c_idx))
    while to_flash:
        oct_r, oct_c = to_flash.pop()
        for x, y in neighbors:
            u, v = oct_r + x, oct_c + y
            if u in {0, 11} or v in {0, 11}:
                continue
            octopi[u][v] += 1
            if flashes[u][v] == 0 and octopi[u][v] > 9:
                flashes[u][v] = 1
                total_flashes += 1
                to_flash.append((u, v))
    for r_idx, row in enumerate(flashes[1:-1], 1):
        for c_idx, col in enumerate(row[1:-1], 1):
            if col:
                octopi[r_idx][c_idx] = 0
                flashes[r_idx][c_idx] = 0
    return total_flashes
    # return octopi, flashes

    # flash = True
    # while flash:
    #     flash = False
    #     for r_idx, row in enumerate(octopi[1:-1], 1):
    #         for c_idx, col in enumerate(row[1:-1], 1):
    #             if col == 9 and flashes[r_idx][c_idx] == 0:
    #                 flashes[r_idx][c_idx] = 1
    #                 flash = True
    #             else:
    #                 neighbor_flashes = 0
    #                 for x, y in neighbors:
    #                     if octopi[r_idx+x][c_idx+y]


def get_octopi():
    with open(args.f, "r") as f:
        octopi = []
        for line in f:
            octopi.append([0] + list(map(int, list(line.strip()))) + [0])
    octopi.append([0 for _ in octopi[0]])
    octopi.insert(0, [0 for _ in octopi[0]])
    flashes = [[0 for _ in row] for row in octopi]
    return octopi, flashes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
