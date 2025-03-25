import argparse


class Die:
    def __init__(self):
        self.val = 0
        self.rolls = 0

    def roll(self):
        self.val += 1
        if self.val > 100:
            self.val = 1
        self.rolls += 1
        return self.val


class Pawn:
    def __init__(self, pos, die):
        self.pos = pos
        self.score = 0
        self.die = die

    def roll(self):
        self.pos += self.die.roll()
        if self.pos > 10:
            self.pos %= 10
            if not self.pos:
                self.pos = 10

    def turn(self):
        for _ in range(3):
            self.roll()
        self.score += self.pos
        if self.score >= 1000:
            return self.score


class DiracDice:
    def __init__(self, pos1, pos2):
        self.die = Die()
        self.pawns = [Pawn(pos1, self.die), Pawn(pos2, self.die)]
        self.player = 0

    def turn(self):
        if self.pawns[self.player].turn():
            return True
        self.player ^= 1

    def play(self):
        winner = False
        while not winner:
            winner = self.turn()
        return self.pawns[self.player ^ 1].score * self.die.rolls


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p1", type=int)
    parser.add_argument("p2", type=int)
    args = parser.parse_args()
    game = DiracDice(args.p1, args.p2)
    print(game.play())
