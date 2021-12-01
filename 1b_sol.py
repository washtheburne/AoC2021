import argparse


def find_window_increase(infile):
    last_three = [None, None, None]
    rot = 0
    increases = 0
    with open(infile, "r") as f:
        for i in range(3):
            last_three[i] = int(next(f).strip())
        for line in f:
            val = int(line.strip())
            if val > last_three[rot]:
                increases += 1
            last_three[rot] = val
            rot = (rot + 1) % 3
    return increases


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    increases = find_window_increase(args.f)
    print(increases)
