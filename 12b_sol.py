import argparse


class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.lower = True


class CaveMap:
    def __init__(self):
        self.caves = {}
        self.build_map()

    def parse_line(self, line):
        edge = line.strip().split("-")
        for cave in edge:
            if cave not in self.caves:
                self.caves[cave] = Node(cave)
                if cave.lower() != cave:
                    self.caves[cave].lower = False
        self.caves[edge[0]].neighbors.add(self.caves[edge[1]])
        self.caves[edge[1]].neighbors.add(self.caves[edge[0]])

    def build_map(self):
        with open(args.f, "r") as f:
            for line in f:
                self.parse_line(line)

    def cave_travel(self, cave, path=[], resmall=False):
        if cave.label == "end":
            path.append(cave.label)
            return 1
        downstream = 0
        for nbr in cave.neighbors:
            if nbr.label == "start":
                continue
            if nbr.lower and (nbr.label in path):
                if resmall:
                    continue
                downstream += self.cave_travel(nbr, path + [cave.label], True)
            else:
                downstream += self.cave_travel(nbr, path + [cave.label], resmall)
        return downstream


def main():
    cave_map = CaveMap()
    print(cave_map.cave_travel(cave_map.caves["start"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
