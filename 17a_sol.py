import argparse
from math import sqrt


class Solution:
    def __init__(self):
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.apogee = 0

    def get_bounds(self, infile):
        with open(infile, "r") as f:
            self.x_min = int(next(f).strip())
            self.x_max = int(next(f).strip())
            self.y_min = int(next(f).strip())
            self.y_max = int(next(f).strip())

    def tri(self, n):
        return int((n * (n + 1)) / 2)

    def land(self, apogee):
        if self.y_max + apogee >= 0:
            steps = int((1 + sqrt(1 + 8 * (self.y_max + apogee))) / 2)
            # print(steps, apogee)
            for i in range(steps - 1, steps + 3):
                pos = apogee - (((i) * (i - 1)) // 2)
                if self.y_min <= pos <= self.y_max:
                    # print("True")
                    return True
        return False

    def max_height(self):
        max_apogee = 0
        for i in range(1, 1000):
            apogee = self.tri(i)
            if apogee > self.y_max and self.land(apogee):
                # break
                max_apogee = apogee
        return max_apogee


def main(infile):
    shot = Solution()
    shot.get_bounds(infile)
    print(shot.max_height())


#     def x_vel_range(self):
#         # I believe this function
#         lower = int((1 + sqrt(1 + 8 * self.x_min)) / 2)
#         return lower, self.x_max + 1

#     def y_vel_bound(self, y_bound, steps):
#         return int(y_bound / steps + (steps - 1) * (steps - 2) / (2 * steps))

#     def y_vel_range(self, steps):
#         min_vel = self.y_vel_bound(self.y_min, steps)
#         max_vel = self.y_vel_bound(self.y_max, steps) + 1
#         return min_vel, max_vel

#     def get_steps(self, x_vel):
#         # I believe this function
#         x_pos = 0
#         min_steps = 0
#         while x_pos < self.x_min:
#             x_pos += x_vel
#             min_steps += 1
#             if x_vel > 0:
#                 x_vel -= 1
#             elif x_vel < 0:
#                 x_vel += 1
#             else:
#                 if x_min <= x_pos <= x_max:
#                     return min_steps, min_steps + self.y_max - self.y_min
#                 else:
#                     return 0, 0
#         max_steps = min_steps
#         while x_pos <= self.x_max:
#             max_steps += 1
#             x_pos += x_vel
#             if x_vel > 0:
#                 x_vel -= 1
#             elif x_vel < 0:
#                 x_vel += 1
#             else:
#                 return min_steps, max_steps + self.y_max - self.y_min
#         if max_steps == min_steps:
#             return 0, 0
#         return min_steps, max_steps + 1

#     def trajectory(self, x_vel, y_vel, steps):
#         local_max = 0
#         in_box = False
#         y_pos = 0
#         x_pos = 0
#         for step in range(steps):
#             x_pos += x_vel
#             y_pos += y_vel
#             if x_vel > 0:
#                 x_vel -= 1
#             elif x_vel < 0:
#                 x_vel += 1
#             y_vel -= 1
#             if self.x_min <= x_pos <= self.x_max:
#                 if self.y_min <= y_pos <= self.y_max:
#                     in_box = True
#             if y_pos > local_max:
#                 local_max = y_pos
#         if in_box:
#             if local_max > self.apogee:
#                 self.apogee = local_max


# def main(infile):
#     shot = Solution()
#     shot.get_bounds(infile)
#     xv_min, xv_max = shot.x_vel_range()
#     print(xv_min, xv_max)
#     for x_vel in range(xv_min, xv_max):
#         min_steps, max_steps = shot.get_steps(x_vel)
#         if max_steps:
#             print(x_vel, min_steps, max_steps)
#             for steps in range(min_steps, max_steps):
#                 yv_min, yv_max = shot.y_vel_range(steps)
#                 for y_vel in range(yv_min, yv_max):
#                     shot.trajectory(x_vel, y_vel, steps)
#     print(shot.apogee)


# def get_pos(x_vel, y_vel, steps):
#     if x_vel >= 0:
#         x_steps = min(steps, x_vel)
#         x = x_vel * x_steps - sum(range(x_steps))
#     else:
#         x_steps = min(steps, -x_vel)
#         x = x_vel * x_steps - sum(range(x_steps))
#     y = y_vel * steps - sum(range(steps))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
