from collections import defaultdict

def parse_rules(rule_list):
    adjacency_list = defaultdict(list)
    for rule in rule_list:
        x, y = map(int, rule.split('|'))
        adjacency_list[x].append(y)
    return adjacency_list


def is_valid_update(update, adjacency_list):
    for x in adjacency_list:
        for y in adjacency_list[x]:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

def main(filename):
    total = 0
    converted_lists = []

    with open(filename, "r") as f:
        input_list = f.read().split("\n")
        idx = input_list.index('')

        undefined_rules = input_list[:idx]
        pages = input_list[idx:]

    rules = parse_rules(undefined_rules)


    for item in pages:
        if item:
            converted_lists.append([int(num) for num in item.split(',')])

    for update in converted_lists:
        if is_valid_update(update, rules):  # Check if the update is valid
            middle_page = get_middle_page(update)  # Get the middle page number
            total += middle_page  # Add to the total sum

    print(f"Total sum of middle page numbers: {total}")

if __name__ == "__main__":
    main("input/day_05.txt")

