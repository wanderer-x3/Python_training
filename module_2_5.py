def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([value] * m)
        # for j in range(m):
        #     j < m
        #     matrix.insert(j, value)
    print(matrix)

get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
