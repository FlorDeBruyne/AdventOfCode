import re
import numpy as np


def extract_mul_instructions(line):
    p1_sum = 0
    p2_sum = 0
    part_2 = True

    for i, _, x, y in re.findall(r"(mul|don't|do)\(((\d+),(\d+)|)\)", line):
        if i == "mul":
            sum_result = (int(x) * int(y))
            p1_sum += sum_result
            if part_2:
                p2_sum += sum_result

        if i == "don't":
            part_2 = False
        if i == "do":
            part_2 = True

    return p1_sum, p2_sum


def multiply_and_sum(pairs):
    # Multiply each pair and sum the results
    return sum(x * y for x, y in pairs)


def main(filename):
    total_sum_p1 = 0
    total_sum_p2 = 0
    with open(filename, 'r') as f:
        sums = extract_mul_instructions(f.read())
        total_sum_p1 += sums[0]
        total_sum_p2 += sums[1]

    return total_sum_p1, total_sum_p2


if __name__ == "__main__":
    input_file = "input/day_03.txt"
    result = main(input_file)
    print(result)
