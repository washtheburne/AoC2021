import argparse


def increment_pop(timers):
    births = timers[0]
    for i in range(8):
        timers[i] = timers[i + 1]
    timers[8] = births
    timers[6] += births


def main():
    timers = [0 for _ in range(9)]
    with open(args.f, "r") as f:
        for fish in next(f).strip().split(","):
            timers[int(fish)] += 1
    for i in range(256):
        increment_pop(timers)
    print(sum(timers))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
