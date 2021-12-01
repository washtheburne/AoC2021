import argparse


def find_increase(infile):
    last_val = float("inf")
    increases = 0
    with open(infile, "r") as f:
        for line in f:
            val = int(line.strip())
            if val > last_val:
                increases += 1
            last_val = val
    return increases


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    increases = find_increase(args.f)
    print(increases)
