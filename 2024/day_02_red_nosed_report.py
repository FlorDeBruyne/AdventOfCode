def check_order(input_list) -> bool:
    input_list = list(map(int, input_list))
    if sorted(input_list) == input_list:
        return True
    if sorted(input_list, reverse=True) == input_list:
        return True
    return False

def check_difference(input_list):
    input_list = list(map(int, input_list))
    for idx in range(len(input_list) - 1):
        diff = abs(input_list[idx] - input_list[idx + 1])
        if 1 <= diff <= 3:
            continue
        else:
            return False, idx
    return True, None

def problem_dampener(input_list) -> bool:
    for i in range(len(input_list)):
        temp_list = input_list[:i] + input_list[i+1:]
        if check_order(temp_list) and check_difference(temp_list)[0]:
            return True
    return False

def main(input_list) -> bool:
    if check_order(input_list) and check_difference(input_list)[0]:
        return True

    return problem_dampener(input_list)

if __name__ == "__main__":
    outputs = []
    with open("/home/flor/Workspace/AdventOfCode/2024/input_day_02.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            input_list = line.strip().split()
            value = main(input_list)
            outputs.append(value)
    print(outputs.count(True))
381