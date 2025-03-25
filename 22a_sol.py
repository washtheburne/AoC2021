import argparse


def build_reactor():
    reactor = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    return reactor


def reboot(inst, reactor):
    with open(inst, "r") as f:
        for row in f:
            toggle, cuboid = row.strip().split(" ")
            if toggle == "on":
                toggle = 1
            else:
                toggle = 0
            x, y, z = [c.split("=")[1] for c in cuboid.split(",")]
            x_min, x_max = list(map(int, x.split("..")))
            y_min, y_max = list(map(int, y.split("..")))
            z_min, z_max = list(map(int, z.split("..")))
            if max(x_max, y_max, z_max) > 50 or min(x_min, y_min, z_min) < -50:
                continue
            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    for z in range(z_min, z_max + 1):
                        reactor[x + 50][y + 50][z + 50] = toggle
    on_cubes = sum(sum(sum(z) for z in y) for y in reactor)
    return on_cubes


def main():
    reactor = build_reactor()
    on_cubes = reboot(args.f, reactor)
    print(on_cubes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
