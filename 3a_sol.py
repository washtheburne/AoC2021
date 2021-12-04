import argparse


def get_power(infile):
    with open(infile, "r") as f:
        freq = next(f).strip()
        freq = [1 if c == "1" else -1 for c in freq]
        for line in f:
            for i, c in enumerate(line.strip()):
                if c == "1":
                    freq[i] += 1
                else:
                    freq[i] -= 1
    gamma = 0
    epsilon = 0
    for x in freq:
        gamma <<= 1
        epsilon <<= 1
        if x > 0:
            gamma ^= 1
        else:
            epsilon ^= 1
    return gamma * epsilon


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    print(get_power(args.f))
