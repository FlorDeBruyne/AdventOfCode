import re
import numpy as np


def extract_mul_instructions(line):
    # Match valid `mul(X,Y)` patterns
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)
    # Convert matches to a list of integer pairs

    return [(int(x), int(y)) for x, y in matches]


def multiply_and_sum(pairs):
    # Multiply each pair and sum the results
    return sum(x * y for x, y in pairs)


def main(filename):
    total_sum = 0
    with open(filename, 'r') as f:
        for line in f:
            mul_pairs = extract_mul_instructions(line)
            total_sum += multiply_and_sum(mul_pairs)

    return total_sum


if __name__ == "__main__":
    input_file = "/home/flor/Workspace/AdventOfCode/2024/input/input_day_03.txt"
    result = main(input_file)
    print(result)