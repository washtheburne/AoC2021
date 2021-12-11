import argparse

complete = {"(": 1, "[": 2, "{": 3, "<": 4}
lefts = ["(", "[", "<", "{"]
rights = [")", "]", ">", "}"]
pair = {x: y for x, y in zip(rights, lefts)}
close = {y: x for x, y in pair.items()}


def main():
    scores = []
    with open(args.f, "r") as f:
        for line in f:
            s = line_score(line.strip())
            if s:
                scores.append(s)
            # scores.append(line_score(line.strip()))
    scores.sort()
    mid_score = scores[len(scores) // 2]
    print(mid_score)


def line_score(paren_string):
    opens = []
    for c in paren_string:
        if c in lefts:
            opens.append(c)
        else:
            if opens:
                if pair[c] != opens.pop():
                    return 0
            else:
                return 0
    return autocomplete(opens)


def autocomplete(opens):
    score = 0
    for c in opens[::-1]:
        score *= 5
        score += complete[c]
    return score


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
