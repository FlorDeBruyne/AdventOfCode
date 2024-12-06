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
                index_x = update.index(x)
                index_y = update.index(y)
                if index_x > index_y:
                    return False, update
    return True, None
def change_position(index_01, index_02, adjacency_list):
    num_01, num_02 = adjacency_list[index_01], adjacency_list[index_02]
    adjacency_list[index_01], adjacency_list[index_02] = num_02, num_01
    return adjacency_list

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

    bad_updates = []
    for update in converted_lists:
        valid, bad_update = is_valid_update(update, rules)
        bad_updates.append(bad_update)

    for bad_update in bad_updates:
        # Check if the update is valid
        update = change_position(index_x, index_y, update)
        middle_page = get_middle_page(update)  # Get the middle page number
        total += middle_page  # Add to the total sum

    print(f"Total sum of middle page numbers: {total}")

if __name__ == "__main__":
    main("input/day_05.txt")

