from collections import namedtuple, defaultdict
import sys
import math

class IVec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return IVec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return IVec2(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"IVec2({self.x}, {self.y})"

def scan(map, pos):
    if map.get(pos - IVec2(1, 0), '').isdigit():
        return None

    p, s = pos, ''
    while (c := map.get(p, '')).isdigit():
        s += c
        p += IVec2(1, 0)

    if not s:
        return None

    gear, symbol_found = None, False
    bounds = [(x, y) for x in range(pos.x - 1, p.x + 1) for y in range(pos.y - 1, pos.y + 2)]

    for x, y in bounds:
        c = map.get(IVec2(x, y), '')
        if c == '*':
            gear = IVec2(x, y)
        if c not in '.0123456789':
            symbol_found = True

    return (int(s), gear) if symbol_found else None

def main():
    cloud, y = {}, 0
    for line in sys.stdin:
        for x, c in enumerate(line.strip()):
            cloud[IVec2(x, y)] = c
        y += 1

    parts = [scan(cloud, k) for k in cloud]
    parts = [p for p in parts if p]

    print(sum(n for n, _ in parts))

    gears = defaultdict(list)
    for n, g in parts:
        if g:
            gears[g].append(n)

    ratios = sum(math.prod(parts) for parts in gears.values() if len(parts) > 1)
    print(ratios)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
