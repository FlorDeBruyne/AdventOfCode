def operation_check(input_list):
    operations = ['+', '*']

    for ope in operations:
        for idx, item in input_list:
            solution = input_list[idx][0]
            numbers = input_list[idx][1]
            for item in range(len(numbers)-1):
                e





def main(filename):

    input_list = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n").split(":")
            input_list.append((line[0], line[1].split()))
            
    print(input_list)




if __name__ == "__main__":
    print(main("/home/flor/Workspace/AdventOfCode/2024/input/day_07.txt"))