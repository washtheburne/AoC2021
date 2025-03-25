import functools
from itertools import product
import argparse

rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@functools.lru_cache(maxsize=None)
def play_out(p1, p2, s1, s2, w1, w2, player):
    wins = [w1, w2]
    # for d1, d2, d3 in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
    for roll, freq in rolls.items():
        pos = [p1, p2]
        scores = [s1, s2]
        # roll = d1 + d2 + d3
        new_pos = (roll + pos[player]) % 10
        if new_pos == 0:
            new_pos = 10
        pos[player] = new_pos
        scores[player] += new_pos
        if scores[player] >= 21:
            wins[player] += freq
        else:
            x, y = play_out(pos[0], pos[1], scores[0], scores[1], 0, 0, player ^ 1)
            wins[0] += x * freq
            wins[1] += y * freq
    return wins


def main():
    universes = play_out(args.p1, args.p2, 0, 0, 0, 0, 0)
    print(max(universes))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p1", type=int)
    parser.add_argument("p2", type=int)
    args = parser.parse_args()
    main()
