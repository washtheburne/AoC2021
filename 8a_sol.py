import argparse


def main():
    uniques = 0
    with open(args.f, "r") as f:
        for line in f:
            for output in line.split("|")[1].split():
                if len(output) in {2, 3, 4, 7}:
                    uniques += 1
    print(uniques)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
