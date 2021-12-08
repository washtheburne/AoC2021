import argparse


def main():
    with open(args.f, "r") as f:
        crabs = sorted(list(map(int, next(f).strip().split(","))))
    center = crabs[len(crabs) // 2]
    print(sum(abs(x - center) for x in crabs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
