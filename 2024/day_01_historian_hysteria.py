def total_distance(list_1, list_2):
    assert len(list_1) == len(list_2), "The both lists need to have the same length"
    list_1, list_2 = sorted(list_1), sorted(list_2)
    distances = []

    for i in range(len(list_1)):
        distances.append(abs(list_1[i] - list_2[i]))
    
    return sum(distances)


def similarity_score(list_1, list_2):
    sim = []
    for item in range(len(list_1)):
        sim.append(list_1[item] * lookup_number(list_1[item], list_2))
    return sum(sim)



def lookup_number(number, list_2):
    amount = list_2.count(number)
    total = amount if amount>0 else 0
    return total 


if __name__ == "__main__":
    list_1 = []
    list_2 = []
    with open("/home/flor/Workspace/AdventOfCode/2024/input_list.txt", "r") as f:
        line = f.readlines()
        for i in range(0, len(line), 1):
            [n1, n2] = line[i].split()
            list_1.append(int(n1))
            list_2.append(int(n2))

    print(similarity_score(list_1, list_2))
    

