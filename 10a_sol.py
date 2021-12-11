import argparse

illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}
lefts = ["(", "[", "<", "{"]
rights = [")", "]", ">", "}"]
pair = {x: y for x, y in zip(rights, lefts)}


def main():
    score = 0
    with open(args.f, "r") as f:
        for line in f:
            score += line_score(line.strip())
    print(score)


def line_score(paren_string):
    opens = []
    for c in paren_string:
        if c in lefts:
            opens.append(c)
        else:
            if opens:
                if pair[c] != opens.pop():
                    return illegal[c]
            else:
                return illegal[c]
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
