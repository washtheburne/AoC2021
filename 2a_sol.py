import argparse


def sub_travel(infile):
    pos = [0, 0]
    with open(infile, "r") as f:
        for row in f:
            inst, val = row.strip().split()
            if inst == "forward":
                pos[0] += int(val)
            elif inst == "down":
                pos[1] += int(val)
            elif inst == "up":
                pos[1] -= int(val)
    return pos[0] * pos[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    print(sub_travel(args.f))
