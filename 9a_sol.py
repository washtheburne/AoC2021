import argparse


def check_line(prev, row, nxt):
    line_risk = 0
    for idx, dep in enumerate(row[1:-1], 1):
        if (
            prev[idx] > dep
            and nxt[idx] > dep
            and row[idx - 1] > dep
            and row[idx + 1] > dep
        ):
            line_risk += dep + 1
    return line_risk


def main():
    risk = 0
    with open(args.f, "r") as f:
        row = [10] + list(map(int, list(next(f).strip()))) + [10]
        nxt = [10] + list(map(int, list(next(f).strip()))) + [10]
        prev = [10 for x in row]
        for line in f:
            risk += check_line(prev, row, nxt)
            prev = row
            row = nxt
            nxt = [10] + list(map(int, list(line.strip()))) + [10]
        prev = row
        row = nxt
        nxt = [10 for x in row]
        risk += check_line(prev, row, nxt)
    print(risk)


def big_main():
    floor_map = []
    risk = []
    with open(args.f, "r") as f:
        for line in f:
            floor_map.append([10] + list(map(int, list(line.strip()))) + [10])
    floor_map.append([10 for _ in floor_map[-1]])
    floor_map.insert(0, [10 for _ in floor_map[-1]])
    neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for r_idx, row in enumerate(floor_map[1:-1], 1):
        for c_idx, col in enumerate(row[1:-1], 1):
            if min([floor_map[r_idx + x][c_idx + y] for x, y in neighbors]) > col:
                risk.append(col)
    total_risk = len(risk) + sum(risk)
    print(total_risk)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    big_main()
    # why does main give 494 instead of 496?
