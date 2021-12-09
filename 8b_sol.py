import argparse

# wires = {
#     "cf": 1,
#     "acf": 7,
#     "bcdf": 4,
#     "acdeg": 2,
#     "acdfg": 3,
#     "abdfg": 5,
#     "abcefg": 0,
#     "abdefg": 6,
#     "abcdfg": 9,
#     "abcdefg": 8,
# }


def parse_line(line):
    digits, output = line.split("|")
    crossed_wires = calc_digits(digits)
    output_value = read_outputs(output, crossed_wires)
    return output_value


def calc_digits(digits):
    crossed_wires = [None for _ in range(10)]
    u_segs = set(digits.split())
    nu_segs = set()
    for digit in u_segs:
        if len(digit) == 2:
            crossed_wires[1] = "".join(sorted(digit))
        elif len(digit) == 3:
            crossed_wires[7] = "".join(sorted(digit))
        elif len(digit) == 4:
            crossed_wires[4] = "".join(sorted(digit))
        elif len(digit) == 7:
            crossed_wires[8] = "".join(sorted(digit))
        else:
            nu_segs.add("".join(sorted(digit)))
    # a = crossed_wires[7] - crossed_wires[1]
    for digit in nu_segs:
        if len(digit) == 6:
            if len(set(digit).intersection(set(crossed_wires[7]))) == 2:
                crossed_wires[6] = digit
            elif len(set(digit).intersection(set(crossed_wires[4]))) == 4:
                crossed_wires[9] = digit
            else:
                crossed_wires[0] = digit
        else:
            if len(set(digit).intersection(set(crossed_wires[7]))) == 3:
                crossed_wires[3] = digit
            elif len(set(digit).intersection(set(crossed_wires[4]))) == 3:
                crossed_wires[5] = digit
            else:
                crossed_wires[2] = digit
    crossed_wires = {s: i for i, s in enumerate(crossed_wires)}
    return crossed_wires


def read_outputs(output, digits):
    val = 0
    for segments in output.split():
        val *= 10
        val += digits["".join(sorted(segments))]
    return val


def main():
    out_sum = 0
    with open(args.f, "r") as f:
        for line in f:
            out_sum += parse_line(line)
    print(out_sum)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
