import argparse


def bingo_setup(infile):
    cards = []
    row_wins = []
    col_wins = []
    with open(infile, "r") as f:
        balls = list(map(int, next(f).strip().split(",")))
        card = None
        for line in f:
            card_line = line.strip()
            if card_line == "":
                if card:
                    cards.append(card)
                    row_wins.append([[0 for _ in range(5)] for _ in range(5)])
                    col_wins.append([[0 for _ in range(5)] for _ in range(5)])
                card = []
            else:
                card.append(list(map(int, card_line.split())))
    cards.append(card)
    row_wins.append([[0 for _ in range(5)] for _ in range(5)])
    col_wins.append([[0 for _ in range(5)] for _ in range(5)])
    return balls, cards, row_wins, col_wins


def play_bingo(balls, cards, row_wins, col_wins):
    for ball in balls:
        is_done = check_ball(ball, cards, row_wins, col_wins)
        if is_done:
            return ball * is_done


def check_ball(ball, cards, row_wins, col_wins):
    for idx_b, card in enumerate(cards):
        for idx_r, row in enumerate(card):
            for idx_c, col in enumerate(row):
                if col == ball:
                    row_wins[idx_b][idx_r][idx_c] = 1
                    col_wins[idx_b][idx_c][idx_r] = 1
                    if (
                        sum(row_wins[idx_b][idx_r]) == 5
                        or sum(col_wins[idx_b][idx_c]) == 5
                    ):
                        score = read_score(card, row_wins[idx_b])
                        return score


def read_score(card, wins):
    score = 0
    for i in range(5):
        for j in range(5):
            if wins[i][j] == 0:
                score += card[i][j]
    return score


def main(f):
    balls, cards, row_wins, col_wins = bingo_setup(f)
    score = play_bingo(balls, cards, row_wins, col_wins)
    print(score)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
