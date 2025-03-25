import argparse


def ingest(infile):
    with open(infile, "r") as f:
        enhancement = next(f).strip()
        row = next(f).strip()
        img = []
        for row in f:
            img.append([0 if j == "." else 1 for j in row.strip()])
    return img, enhancement


def get_neighbors(r, c, im, filler):
    bs = ""
    for rm in [-1, 0, 1]:
        for cm in [-1, 0, 1]:
            if r + rm < 0 or r + rm >= len(im) or c + cm < 0 or c + cm >= len(im[0]):
                bs += str(filler)
            else:
                bs += str(im[r + rm][c + cm])
    if en[int(bs, 2)] == "#":
        return 1
    return 0


def seed(img, filler):
    w = len(img[0]) + 2
    new_img = [[filler] * w]
    for row in img:
        new_img.append([filler] + row + [filler])
    new_img.append([filler] * w)
    return new_img


def enhance(img, rd):
    filler = 1 if en[0] == "#" and en[-1] == "." and not rd % 2 else 0
    new_img = seed(img, filler)
    changes = {}
    for r in range(len(new_img)):
        for c in range(len(new_img[0])):
            changes[(r, c)] = get_neighbors(r, c, new_img, filler)
    for r, c in changes:
        new_img[r][c] = changes[(r, c)]
    return new_img


def count_lit(img):
    return sum(sum(row) for row in img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    img, en = ingest(args.f)
    for i in range(1, 3):
        img = enhance(img, i)
    print(count_lit(img))
