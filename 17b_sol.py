import argparse
from math import sqrt


class Solution:
    def __init__(self):
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.y_vels = {}
        self.x_steps = {}
        self.traj_count = 0

    def get_bounds(self, infile):
        with open(infile, "r") as f:
            self.x_min = int(next(f).strip())
            self.x_max = int(next(f).strip())
            self.y_min = int(next(f).strip())
            self.y_max = int(next(f).strip())

    def tri(self, n):
        return int((n * (n + 1)) / 2)

    def land(self, y_vel):
        apogee = self.tri(y_vel)
        if self.y_max - apogee <= 0:
            steps_min = int((1 + sqrt(1 - 8 * (self.y_max - apogee))) / 2)
            for i in range(
                steps_min - 1, steps_min + (self.y_max - self.y_min) // steps_min + 3
            ):
                pos = apogee - (((i) * (i - 1)) // 2)
                if self.y_min <= pos <= self.y_max:
                    if y_vel + i in self.y_vels:
                        self.y_vels[y_vel + i].add(y_vel)
                    else:
                        self.y_vels[y_vel + i] = {y_vel}

    def fill_y(self):
        for i in range(self.y_min, -self.y_min + 1):
            if self.tri(i) > self.y_max:
                self.land(i)

    def x_vel_range(self):
        lower = int((1 + sqrt(1 + 8 * self.x_min)) / 2)
        return range(lower, self.x_max + 1)

    def test_x_vel(self, x_vel):
        x = 0
        steps = 0
        vel = x_vel
        y_vels = set()
        while x < self.x_max:
            x += vel
            vel -= 1
            steps += 1
            if self.x_min <= x <= self.x_max:
                if steps in self.y_vels:
                    y_vels.update(self.y_vels[steps])
                if vel == 0:
                    for s in range(steps + 1, max(self.y_vels.keys()) + 1):
                        if s in self.y_vels:
                            y_vels.update(self.y_vels[s])
                    self.traj_count += len(y_vels)
                    return
        self.traj_count += len(y_vels)


def main(infile):
    shot = Solution()
    shot.get_bounds(infile)
    shot.fill_y()
    for vel in shot.x_vel_range():
        shot.test_x_vel(vel)
    print(shot.traj_count)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
