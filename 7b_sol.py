import argparse


def fuel(target, source):
    num = abs(target - source) * (abs(target - source) + 1)
    return num // 2


def main():
    with open(args.f, "r") as f:
        crabs = sorted(list(map(int, next(f).strip().split(","))))
    min_cost = float("inf")
    for i in range(crabs[-1]):
        cost = sum(fuel(i, h) for h in crabs)
        if cost > min_cost:
            print(min_cost)
            return
        min_cost = cost


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
