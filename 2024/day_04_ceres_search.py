def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def count_word(array, word):
    string = ''.join(array)
    count = 0
    offset = len(word)
    i = 0
    while i <= len(string) - offset:
        if string[i:i + offset] == word:
            count += 1
            i += offset
        else:
            i += 1
    return count


def search_word(matrix, word):
    count = 0
    for _ in range(4):
        for i in range(len(matrix)):
            count += count_word(matrix[i], word)
            diagonal = ''
            for j in reversed(range(i + 1)):
                diagonal += matrix[i - j][j]
            count += count_word(diagonal, word)
            if not (i == len(matrix) - 1):  # prevent counting middle (largest) diagonal(s) twice
                count += count_word(diagonal[::-1], word)
        matrix = rotate_matrix(matrix)
    return count


def search_X_MAS(matrix):
    count = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            diagonal1 = matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]
            diagonal2 = matrix[i - 1][j + 1] + matrix[i][j] + matrix[i + 1][j - 1]
            if (diagonal1 == 'MAS' or diagonal1 == 'SAM') and (diagonal2 == 'MAS' or diagonal2 == 'SAM'):
                count += 1
    return count


if __name__ == '__main__':
    with open("input/day_04.txt", "r") as f:
        character_matrix = [row.strip() for row in f.readlines()]
        print(search_word(character_matrix, 'XMAS'))
        print(search_X_MAS(character_matrix))

