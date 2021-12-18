import argparse


class dotPaper:
    def __init__(self):
        self.dots = set()
        self.folds = []
        self.get_paper()

    def get_paper(self):
        with open(args.f, "r") as f:
            while True:
                line = next(f).strip()
                if line == "":
                    break
                self.dots.add(tuple(map(int, line.split(","))))
            for line in f:
                dim, fold = line.split()[2].split("=")
                self.folds.append((ord(dim) - 120, int(fold)))

    def do_fold(self, dim, line):
        top = set()
        bot = set()
        for dot in self.dots:
            if dot[dim] > line:
                bot.add(dot)
                if dim:
                    top.add((dot[0], 2 * line - dot[1]))
                else:
                    top.add((2 * line - dot[0], dot[1]))
        self.dots.difference_update(bot)
        self.dots.update(top)

    def paper_dim(self):
        max_x = 0
        max_y = 0
        for x, y in self.dots:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        return max_x, max_y

    def draw_paper(self, x, y):
        paper_lines = [["." for _ in range(x + 1)] for _ in range(y + 1)]
        for dot in self.dots:
            paper_lines[dot[1]][dot[0]] = "0"
        for line in paper_lines:
            print("".join(line))


def main():
    paper = dotPaper()
    for fold in paper.folds:
        paper.do_fold(*fold)
    x, y = paper.paper_dim()
    paper.draw_paper(x, y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
