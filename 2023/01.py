from aoc import *

def digit1(s):
    try:
        return int(s[0])
    except (IndexError, ValueError):
        return None

def digit2(s):
    words = ["💩", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, word in enumerate(words):
        if s.startswith(word):
            return i
    return digit1(s)

def main():
    lines = [line.strip() for line in sys.stdin]

    for func in [digit1, digit2]:
        n = 0
        for line in lines:
            a = next(filter(None, map(func, suffixes(line))), None)
            b = None
            for val in filter(None, map(func, suffixes(line))):
                b = val
            if a is not None and b is not None:
                n += a * 10 + b
        print(n)

if __name__ == "__main__":
    import sys
    main()