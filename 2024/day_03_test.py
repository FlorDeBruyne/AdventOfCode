from sys import stdin
import re


if __name__ == "__main__":
    input_file = "input/input_day_03.txt"
    result = 0
    with open(input_file, "r") as f:
        for line in f.readlines():
            mul_extracted = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", line)

            enabled = True
            for instr in mul_extracted:
                if instr == "don't()":
                    enabled = False
                elif instr == "do()":
                    enabled = True
                elif enabled:
                    n1, n2 = instr[4:len(instr) - 1].split(",")

                    result += int(n1) * int(n2)
        print(result)