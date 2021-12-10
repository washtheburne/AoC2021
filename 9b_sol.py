import argparse

neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
floor_map = []


def basin_area(r_idx, c_idx):
    if floor_map[r_idx][c_idx] >= 9:
        return 0
    area = 1
    floor_map[r_idx][c_idx] = 9
    for x, y in neighbors:
        area += basin_area(r_idx + x, c_idx + y)
    return area


def big_main():
    basins = []
    with open(args.f, "r") as f:
        for line in f:
            floor_map.append([10] + list(map(int, list(line.strip()))) + [10])
    floor_map.append([10 for _ in floor_map[-1]])
    floor_map.insert(0, [10 for _ in floor_map[-1]])
    for r_idx, row in enumerate(floor_map[1:-1], 1):
        for c_idx, col in enumerate(row[1:-1], 1):
            if col < 9:
                basins.append(basin_area(r_idx, c_idx))
    basins = sorted(basins)
    print(basins[-3] * basins[-2] * basins[-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    big_main()
