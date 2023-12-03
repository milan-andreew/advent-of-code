import sys
import argparse
from typing import Tuple, List, Dict

def parse_args() -> argparse.Namespace:
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Process color draws and calculate scores.")
    parser.add_argument("--red_threshold", type=int, default=12, help="Threshold for red color")
    parser.add_argument("--green_threshold", type=int, default=13, help="Threshold for green color")
    parser.add_argument("--blue_threshold", type=int, default=14, help="Threshold for blue color")
    return parser.parse_args()

def parse_draw(draw: str) -> Tuple[int, int, int]:
    """
    Parses a draw string and returns a tuple of (red, green, blue) values.
    """
    colors = {"red": 0, "green": 0, "blue": 0}
    for elt in draw.split(", "):
        n = int(''.join(filter(str.isdigit, elt)))
        for color in colors:
            if color in elt:
                colors[color] = n
                break
        else:
            raise ValueError(f"Unknown color in element: {elt}")
    return colors["red"], colors["green"], colors["blue"]

def process_input_line(line: str) -> List[Tuple[int, int, int]]:
    """
    Processes a single input line and returns a list of (red, green, blue) tuples.
    """
    return [parse_draw(draw) for draw in line.strip().split(": ")[1].split("; ")]

def calculate_scores(input_data: List[List[Tuple[int, int, int]]], 
                     thresholds: Dict[str, int]) -> Tuple[int, int]:
    """
    Calculates and returns the scores based on the input data and thresholds.
    """
    p1 = 0
    p2 = 0

    for i, play in enumerate(input_data):
        r, g, b = max(play)
        if r <= thresholds["red"] and g <= thresholds["green"] and b <= thresholds["blue"]:
            p1 += i + 1
        p2 += r * g * b

    return p1, p2

def main():
    args = parse_args()

    thresholds = {
        "red": args.red_threshold,
        "green": args.green_threshold,
        "blue": args.blue_threshold
    }

    input_data = [process_input_line(line) for line in sys.stdin]
    p1, p2 = calculate_scores(input_data, thresholds)

    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
