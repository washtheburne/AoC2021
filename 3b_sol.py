import argparse


class Node:
    def __init__(self, freq=0):
        self.zero = None
        self.one = None
        self.val = None
        self.freq = freq


def get_ratings(infile):
    root = Node()
    with open(infile, "r") as f:
        for line in f:
            node = root
            val = line.strip()
            for c in val:
                if c == "0":
                    if node.zero:
                        node.zero.freq += 1
                    else:
                        node.zero = Node(1)
                    node = node.zero
                else:
                    if node.one:
                        node.one.freq += 1
                    else:
                        node.one = Node(1)
                    node = node.one
            node.val = val
    node = root
    while not node.val:
        if node.one and node.zero:
            if node.one.freq >= node.zero.freq:
                node = node.one
            else:
                node = node.zero
        elif node.one:
            node = node.one
        else:
            node = node.zero
    oxy = int(node.val, 2)
    node = root
    while not node.val:
        if node.one and node.zero:
            if node.one.freq >= node.zero.freq:
                node = node.zero
            else:
                node = node.one
        elif node.one:
            node = node.one
        else:
            node = node.zero
    carbox = int(node.val, 2)
    return oxy * carbox


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    print(get_ratings(args.f))
