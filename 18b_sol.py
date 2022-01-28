import argparse
from itertools import permutations


class Node:
    def __init__(self, depth):
        self.depth = depth
        self.left = None
        self.right = None
        self.parent = None
        self.val = None

    def magnitude(self):
        if self.left.val is not None:
            left_mag = 3 * self.left.val
        else:
            left_mag = 3 * self.left.magnitude()
        if self.right.val is not None:
            right_mag = 2 * self.right.val
        else:
            right_mag = 2 * self.right.magnitude()
        mag = left_mag + right_mag
        return mag

    def can_explode(self):
        if self.val is not None:
            if self.depth > 4:
                return self.parent
            return False
        x = self.left.can_explode()
        if x:
            return x
        return self.right.can_explode()

    def find_left(self):
        node = self
        while node.parent:
            if node.parent.left == node:
                node = node.parent
            else:
                node = node.parent.left
                while node.val is None:
                    node = node.right
                return node
        return False

    def find_right(self):
        node = self
        while node.parent:
            if node.parent.right == node:
                node = node.parent
            else:
                node = node.parent.right
                while node.val is None:
                    node = node.left
                return node
        return False

    def can_split(self):
        if self.val is not None:
            if self.val >= 10:
                return self
            return False
        x = self.left.can_split()
        if x:
            return x
        else:
            return self.right.can_split()

    def print(self):
        if self.val is not None:
            return str(self.val)
        else:
            left_string = "[" + self.left.print()
            right_string = self.right.print()
            return left_string + "," + right_string + "]"


class snailNumber:
    def __init__(self, s):
        self.root = Node(0)
        self.nodes = {self.root}
        self.from_string(s)

    def from_string(self, s):
        branches = s.split(",")
        node = self.root
        for b in branches:
            for c in b:
                if c == "[":
                    node.left = Node(node.depth + 1)
                    node.left.parent = node
                    node = node.left
                    self.nodes.add(node)
                elif c == "]":
                    node = node.parent
                else:
                    node.val = int(c)
            if node.parent:
                node = node.parent
                node.right = Node(node.depth + 1)
                node.right.parent = node
                node = node.right
                self.nodes.add(node)
        # return root

    def add(self, snail_number):
        self.nodes.update(snail_number.nodes)
        for node in self.nodes:
            node.depth += 1
        root = Node(0)
        self.nodes.add(root)
        root.left = self.root
        root.left.parent = root
        root.right = snail_number.root
        root.right.parent = root
        self.root = root

    def reduce(self):
        while True:
            x = self.root.can_explode()
            if x:
                self.explode(x)
                continue
            else:
                y = self.root.can_split()
                if y:
                    self.split(y)
                    continue
            break

    def explode(self, node):
        left = node.left.val
        right = node.right.val
        self.nodes.remove(node.left)
        self.nodes.remove(node.right)
        node.left = None
        node.right = None
        node.val = 0
        x = node.find_left()
        y = node.find_right()
        if x:
            x.val += left
        if y:
            y.val += right

    def split(self, node):
        half = node.val // 2
        node.left = Node(node.depth + 1)
        node.right = Node(node.depth + 1)
        node.left.parent = node
        node.right.parent = node
        node.left.val = half
        node.right.val = half + (node.val % 2)
        self.nodes.update({node.left, node.right})
        node.val = None

    def magnitude(self):
        return self.root.magnitude()

    def print(self):
        print(self.root.print())


def main(infile):
    snail_numbers = set()
    with open(infile, "r") as f:
        for row in f:
            snail_numbers.add(row.strip())
    max_sum_mag = 0
    for x, y in permutations(snail_numbers, 2):
        a = snailNumber(x)
        a.reduce()
        b = snailNumber(y)
        b.reduce()
        a.add(b)
        a.reduce()
        mag = a.magnitude()
        if mag > max_sum_mag:
            max_sum_mag = mag
        a = snailNumber(y)
        a.reduce()
        b = snailNumber(x)
        b.reduce()
        a.add(b)
        a.reduce()
        mag = a.magnitude()
        if mag > max_sum_mag:
            max_sum_mag = mag
    print(max_sum_mag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
