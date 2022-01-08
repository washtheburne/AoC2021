import argparse
import heapq


class Cavern:
    def __init__(self):
        self.cavern = None
        self.seen = None
        self.risk = None
        self.depth = 0
        self.width = 0
        self.stack = [(0, (0, 0))]
        # heapq.heapify(self.stack)

    def get_cavern(self, infile):
        cavern = []
        with open(infile, "r") as f:
            for row in f:
                cavern.append([int(i) for i in row.strip()])
        # cavern[0][0] = 0
        tile = cavern
        self.cavern = tile
        for _ in range(4):
            tile = self.repeat(tile)
            for i in range(len(self.cavern)):
                self.cavern[i].extend(tile[i])
        tile = self.cavern
        for _ in range(4):
            tile = self.repeat(tile)
            self.cavern.extend(tile)
        self.cavern[0][0] = 0
        self.depth = len(cavern)
        self.width = len(cavern[0])
        self.risk = [[0 for x in range(self.width)] for y in range(self.depth)]
        self.seen = [[False for x in range(self.width)] for y in range(self.depth)]
        self.seen[0][0] = True

    def repeat(self, tile):
        new_tile = []
        for row in tile:
            new_tile.append([x + 1 if x < 9 else 1 for x in row])
        return new_tile

    # def get_risk(cavern):
    #     for i in range(1, len(cavern[0])):
    #         cavern[0][i] += cavern[0][i - 1]
    #     for i in range(1, len(cavern)):
    #         cavern[i][0] += cavern[i - 1][0]
    #     for i in range(1, len(cavern)):
    #         for j in range(1, len(cavern[i])):
    #             cavern[i][j] += min(cavern[i - 1][j], cavern[i][j - 1])
    #     return cavern[-1][-1]

    def neighbors(self, i, j):
        nbrs = []
        if i > 0:
            nbrs.append((i - 1, j))
        if i < self.depth - 1:
            nbrs.append((i + 1, j))
        if j > 0:
            nbrs.append((i, j - 1))
        if j < self.width - 1:
            nbrs.append((i, j + 1))
        return nbrs

    def try_visit(self, i, j, prisk):
        if self.seen[i][j]:
            if self.risk[i][j] > prisk + self.cavern[i][j]:
                self.risk[i][j] = prisk + self.cavern[i][j]
                # heapq.heappush(self.stack, (self.risk[i][j], (i, j)))
        else:
            self.risk[i][j] = prisk + self.cavern[i][j]
            self.seen[i][j] = True
            heapq.heappush(self.stack, (self.risk[i][j], (i, j)))
        # if not self.seen[i][j]:
        #     self.risk[i][j] = prisk + self.cavern[i][j]
        #     self.seen[i][j] = True
        #     self.stack.append((i, j, self.risk[i][j]))

    def stack_pop(self):
        if not self.stack:
            return  # self.risk[-1][-1]
        prisk, loc = heapq.heappop(self.stack)
        x, y = loc
        for u, v in self.neighbors(x, y):
            self.try_visit(u, v, prisk)
            # if u == self.depth - 1 and v == self.width - 1:
            #     return self.risk[-1][-1]


def main(infile):
    # print(get_risk(get_cavern(infile)))
    cavern = Cavern()
    cavern.get_cavern(args.f)
    while cavern.stack:
        cavern.stack_pop()
    return cavern.risk[-1][-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    print(main(args.f))
