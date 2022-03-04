"""Beautiful Matrix."""


def main():
    matrix = []
    for i in range(5):
        matrix.append(list(map(int, input().split())))

    beautiful_matrix(matrix)


def beautiful_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                print(abs(2 - i) + abs(2 - j))
                break


if __name__ == '__main__':
    main()
