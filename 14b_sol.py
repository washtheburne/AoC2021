import argparse
from collections import Counter


class Polymer:
    def __init__(self, base, inserts):
        self.base = base
        self.inserts = inserts
        self.chars = set(self.inserts.keys())
        self.counts = {}
        self.str_count = {c: 0 for c in self.chars}

    def seed_counts(self):
        for c in self.chars:
            self.counts[c] = {d: [{}] for d in self.chars}
            for d in self.chars:
                self.counts[c][d][0] = {x: 0 for x in self.chars}
                self.counts[c][d][0][c] = 1
            # self.counts[c] = {d: [{x: 0 if x != c else x:1 for x in self.chars}] for d in self.chars}
        self.str_count[self.base[-1]] = 1

    def increment_counts(self, inc):
        for c in self.chars:
            for d in self.chars:
                i = self.inserts[c][d]
                self.counts[c][d].append(
                    {
                        x: self.counts[c][i][inc - 1][x] + self.counts[i][d][inc - 1][x]
                        for x in self.chars
                    }
                )

    def get_sol(self, iters):
        for i in range(1, iters + 1):
            self.increment_counts(i)
        for i in range(len(self.base) - 1):
            for c in self.chars:
                self.str_count[c] += self.counts[self.base[i]][self.base[i + 1]][-1][c]
        hi = max(self.str_count.values())
        lo = min(self.str_count.values())
        return hi - lo


def get_polymer(infile):
    with open(infile, "r") as f:
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


def main():
    base, inserts = get_polymer(args.f)
    shell = Polymer(base, inserts)
    shell.seed_counts()
    print(shell.get_sol(args.i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    parser.add_argument("i", type=int)
    args = parser.parse_args()
    main()
