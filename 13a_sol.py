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


def main():
    paper = dotPaper()
    paper.do_fold(*paper.folds[0])
    print(len(paper.dots))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
