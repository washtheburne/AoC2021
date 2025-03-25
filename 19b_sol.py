import argparse
from itertools import permutations, combinations


class Scanner:
    def __init__(self):
        self.beacons = set()
        self.oriented_beacons = []
        self.pos = (0, 0, 0)

    def orient(self):
        orientations = []
        for x, y, z in permutations([0, 1, 2]):
            orientations.append({(b[x], b[y], b[z]) for b in self.beacons})
            orientations.append({(b[x], -b[y], b[z]) for b in self.beacons})
            orientations.append({(b[x], b[y], -b[z]) for b in self.beacons})
            orientations.append({(b[x], -b[y], -b[z]) for b in self.beacons})
            orientations.append({(-b[x], b[y], b[z]) for b in self.beacons})
            orientations.append({(-b[x], -b[y], b[z]) for b in self.beacons})
            orientations.append({(-b[x], b[y], -b[z]) for b in self.beacons})
            orientations.append({(-b[x], -b[y], -b[z]) for b in self.beacons})
        self.oriented_beacons = orientations

    def delta(self, beacon1, beacon2):
        return tuple(x[1] - x[0] for x in zip(beacon1, beacon2))

    def diff_map(self, orientation):
        this_map = set()
        for x, y in permutations(orientation, 2):
            this_map.add(self.delta(x, y))
        return this_map

    def compare(self, scanner):
        """
        To compare two scanners, consider each orientation of self
        For each orientation, pick a beacon from scanner
        For each beacon of self, calculate the shift to make self.beacon align
        with scanner.beacon
        Given this offset, create a new set shifting all self's beacons by
        this offset
        Calculate cardinality of intersection of new set with
        scanner.beacons
        If cardinality is at least 12, replace self.beacons with this shifted
        set, and reduce self.oriented_beacons to just self.beacons
        """
        if not self.oriented_beacons:
            self.orient()
        target = self.grab(scanner.beacons)
        for target in scanner.beacons:
            for orientation in self.oriented_beacons:
                for beacon in orientation:
                    x, y, z = beacon
                    a, b, c = target
                    offset = (a - x, b - y, c - z)
                    # offset = (x[1] - x[0] for x in zip(beacon, target))
                    shifted_beacons = set()
                    x, y, z = offset
                    for bcn in orientation:
                        a, b, c = bcn
                        shifted_beacons.add((x + a, y + b, z + c))
                    # if offset == (-1304, -1246, -1199):
                    #     print(shifted_beacons)
                    # shifted_beacons = {
                    #     (x[0] + x[1] for x in zip(b, offset)) for b in self.beacons
                    # }
                    # print(shifted_beacons)
                    if len(shifted_beacons.intersection(scanner.beacons)) >= 12:
                        self.beacons = shifted_beacons
                        self.oriented_beacons = shifted_beacons
                        a, b, c = scanner.pos
                        # self.pos = (x - a, y - b, z - c)
                        self.pos = offset
                        return True
                # print("\n")
        return False

    def grab(self, s):
        for e in s:
            ele = e
            break
        return ele


class Solution:
    def __init__(self):
        self.scanners = []
        self.abs_scanners = []
        self.whole_map = set()
        self.max_dist = 0

    def ingest(self, infile):
        with open(infile, "r") as f:
            for row in f:
                if row.strip().startswith("---"):
                    scanner = Scanner()
                    self.scanners.append(scanner)
                elif row.strip() == "":
                    continue
                else:
                    a, b, c = row.strip().split(",")
                    scanner.beacons.add((int(a), int(b), int(c)))
        self.abs_scanners.append(self.scanners.pop(0))

    def align(self):
        while self.scanners:
            c = self.scanners.pop()
            for sc in self.abs_scanners:
                if c.compare(sc):
                    self.abs_scanners.append(c)
                    break
            else:
                self.scanners.insert(0, c)

    def build_map(self):
        for scanner in self.abs_scanners:
            self.whole_map.update(scanner.beacons)

    def how_big(self):
        for x, y in combinations(self.abs_scanners, 2):
            self.max_dist = max(
                self.max_dist,
                (
                    abs(x.pos[0] - y.pos[0])
                    + abs(x.pos[1] - y.pos[1])
                    + abs(x.pos[2] - y.pos[2])
                ),
            )
            # print(self.max_dist, x.pos, y.pos)


def main(infile):
    s = Solution()
    s.ingest(infile)
    s.align()
    s.build_map()
    for sc in s.abs_scanners:
        print(sc.pos)
    # print(s.whole_map)
    s.how_big()
    print(s.max_dist)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
