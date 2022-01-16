import argparse


class ElfBits:
    def __init__(self, str):
        self.string = str
        self.striter = self.str_yield()
        self.bits = 0
        self.tail = 0
        self.bits_read = 0
        self.bit_len = 4 * len(self.string)
        self.packets = []

    def str_yield(self):
        for c in self.string:
            yield c

    def read_nibble(self):
        self.bits += 4
        self.tail <<= 4
        self.tail |= int(next(self.striter), 16)

    def top_k_tail(self, k):
        while self.bits < k:
            self.read_nibble()
        mask = (1 << self.bits) - (1 << (self.bits - k))
        tail_mask = (1 << (self.bits - k)) - 1
        ret = (self.tail & mask) >> (self.bits - k)
        self.tail &= tail_mask
        self.bits -= k
        self.bits_read += k
        return ret


class ElfPkt:
    def __init__(self, bittx):
        self.tx = bittx
        self.tx.packets.append(self)
        self.bit_len = 6
        self.ver = self.tx.top_k_tail(3)
        self.type = self.tx.top_k_tail(3)
        self.mode = None
        self.lit_val = None
        self.child_data = None
        self.children = []
        self.parse_pkt()

    def parse_lit(self):
        while self.tx.bits < 5:
            self.tx.read_nibble()
        not_final = 1
        lit_val = 0
        while not_final:
            while self.tx.bits < 5:
                self.tx.read_nibble()
            chunk = self.tx.top_k_tail(5)
            self.bit_len += 5
            not_final = (chunk & 16) >> 4
            lit_val <<= 4
            lit_val |= chunk & 15
        return lit_val

    def parse_pkt(self):
        if self.type == 4:
            self.lit_val = self.parse_lit()
        else:
            self.mode = self.tx.top_k_tail(1)
            if not self.mode:
                sub_len = self.tx.top_k_tail(15)
                cur = self.tx.bits_read
                while self.tx.bits_read < cur + sub_len:
                    self.children.append(ElfPkt(self.tx))
            else:
                sub_pkts = self.tx.top_k_tail(11)
                for _ in range(sub_pkts):
                    self.children.append(ElfPkt(self.tx))
            if self.type == 0:
                self.lit_val = sum(p.lit_val for p in self.children)
            elif self.type == 1:
                self.lit_val = 1
                for p in self.children:
                    self.lit_val *= p.lit_val
            elif self.type == 2:
                self.lit_val = min(p.lit_val for p in self.children)
            elif self.type == 3:
                self.lit_val = max(p.lit_val for p in self.children)
            elif self.type == 5:
                self.lit_val = self.children[0].lit_val > self.children[1].lit_val
            elif self.type == 6:
                self.lit_val = self.children[0].lit_val < self.children[1].lit_val
            elif self.type == 7:
                self.lit_val = self.children[0].lit_val == self.children[1].lit_val


def main(infile):
    with open(infile, "r") as f:
        for line in f:
            print(line.strip())
            tx = ElfBits(line.strip())
            while tx.bits_read + 4 < tx.bit_len:
                try:
                    ElfPkt(tx)
                except:
                    break
            ver_sum = sum(p.ver for p in tx.packets)
            # print(ver_sum)
            # print(len(tx.packets), "\n")
            print(tx.packets[0].lit_val)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main(args.f)
