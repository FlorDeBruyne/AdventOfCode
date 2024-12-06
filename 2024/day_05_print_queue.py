import re
def set_rules(input_list):
    temp = re.findall(r"\d{1,2}", "".join(x for x in input_list))
    numbers = []
    for i in range(0, len(temp)-2, 2):
        numbers.append((temp[i], temp[i+1]))

    print(numbers)

    rules = []

    for i in range(0, len(numbers)-1):
        num_i = numbers[i]
        for j in range(i, len(numbers)-1):
            num_j = numbers[j]
            if numbers[i] in rules:
                idx_i = rules.index(numbers[i])
                if idx_i != len(rules)-1:
                    if not rules[idx_i+1]:
                        rules[idx_i+1] = numbers[j]
                    elif rules[idx_i+1] == numbers[j]:
                        # print("WRONG?")
                        continue
            else:
                rules.append(numbers[i])

    return rules

if __name__ == "__main__":
    with open("input/day_05.txt", "r") as f:
        input_list = f.read().split("\n")
        idx = input_list.index('')
        undefined_rules = input_list[:idx]
        pages = input_list[idx:]

    rules = set_rules(undefined_rules)


    print(f"Undefined rules: {undefined_rules}")
    print(f"defined rules: {rules}")