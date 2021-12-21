import argparse
from collections import Counter


def get_polymer():
    with open(args.f, "r") as f:
        base = next(f).strip()
        noline = next(f)
        inserts = {}
        for line in f:
            line = line.strip().split()
            pair = line[0]
            ins = line[2]
            if pair[0] in inserts:
                inserts[pair[0]][pair[1]] = ins
            else:
                inserts[pair[0]] = {pair[1]: ins}
    return base, inserts


def do_insert(base, inserts):
    poly = ""
    for i, c in enumerate(base[1:], 1):
        pr = base[i - 1]
        poly += pr
        if base[i - 1] in inserts:
            if c in inserts[pr]:
                poly += inserts[pr][c]
    poly += base[-1]
    return poly


def get_element_counts(base):
    freqs = Counter(base)
    hi, lo = max(freqs.values()), min(freqs.values())
    return hi - lo


def main():
    base, inserts = get_polymer()
    for i in range(40):
        base = do_insert(base, inserts)
    print(get_element_counts(base))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
