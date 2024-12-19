def operation_check(input_list):
    total_sum = 0
    for sol, items in input_list:
        sol = int(sol)
        items = list(map(int, items))
        maxi = max(items)
        for i in range(len(items)-1, 0, -1):
            div = sol / items[i]
            if div == sum(items[:i]):
                total_sum += sol
            else:
                continue

            # if len(items) == 2:
            #     if sol == sum(items) or sol == (items[0]*items[1]):
            #         total_sum += sol
            #         print(f"This solution {sol}, is appended to the total sum: {total_sum}")
            #         continue
            #     else:
            #         continue
            # elif len(items) % 2 == 0:
            #     if sol == sum(items) or (sol/maxi == sum([i for i in items if i != maxi])):
            #         total_sum += sol
            #         print(f"This solution {sol}, is appended to the total sum: {total_sum}")
            #         continue
            #     else:
            #         print(f"This is solution {sol} and items is {items} are even length but not in scope atm")
            # else:
            #     print(f"This is solution {sol} and items is {items}, length is not 2 nor is it even")

    return total_sum

# check if it is possible to obtain an int with the solution divided by the last item from the equation If not possible
# move one item to left and use the sum or product of the two last values to see if there is an int when dividing the
# solution by this number

def main(filename):

    input_list = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n").split(":")
            input_list.append((line[0], line[1].split()))


    total_sum = operation_check(input_list)
    print(f"This is the total sum: {total_sum}")


if __name__ == "__main__":
    print(main("input/day_07.txt"))