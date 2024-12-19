def check_design(possible, design):
    # Keep checking as long as there's something to remove
    while design:
        match_found = False
        for item in possible:
            if item in design:
                print(f"Found '{item}' in design: {design}")
                # Remove only the first occurrence of `item`
                design = design.replace(item, "", 1)
                match_found = True
                break  # Restart the loop to check all possibilities again
        if not match_found:
            print(f"No matches found in design: {design}")
            return False  # Exit if no match is found
    print("Design is empty")
    return True


def main(filename):
    output_list = []
    with open(filename) as f:
        input_list = f.read().split("\n")
        possibilities = input_list[0].split(',')
        designs = input_list[2:]

        for design in designs:
            print(f"\nChecking design: {design}")
            result = check_design(possibilities, design)
            output_list.append(result)

    print(f"\nValid designs count: {output_list.count(True)}")
    return output_list.count(True)


if __name__ == '__main__':
    print(main("input/day_19.txt"))
