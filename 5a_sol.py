import argparse
from collections import defaultdict


def read_vent(line):
    vent = line.strip().split()
    x1, y1 = list(map(int, vent[0].split(",")))
    x2, y2 = list(map(int, vent[2].split(",")))
    if x1 == x2:
        a, b = min(y1, y2), max(y1, y2)
        return [(x1, y) for y in range(a, b + 1)]
    if y1 == y2:
        a, b = min(x1, x2), max(x1, x2)
        return [(x, y1) for x in range(a, b + 1)]


def vent_lines(infile):
    vents = defaultdict(int)
    with open(infile, "r") as f:
        for line in f:
            v = read_vent(line)
            if v:
                for x, y in read_vent(line):
                    vents[(x, y)] += 1
    return vents


def cross_count(vent_lines):
    return sum([1 for y in vent_lines.values() if y > 1])


def main():
    print(cross_count(vent_lines(args.f)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
