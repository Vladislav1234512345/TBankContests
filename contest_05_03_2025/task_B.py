import sys

n, m, k = list(map(int, sys.stdin.readline().split()))
matrix = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))
queries = tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(k))

matrix_prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        matrix_prefix_sum[i][j] = matrix_prefix_sum[i][j - 1] + matrix_prefix_sum[i - 1][j] - matrix_prefix_sum[i - 1][
            j - 1] + matrix[i - 1][j - 1]

for query in queries:
    y1, x1, y2, x2 = query

    result_sum = (matrix_prefix_sum[y2][x2] - matrix_prefix_sum[y2][x1 - 1]) - (
            matrix_prefix_sum[y1 - 1][x2] - matrix_prefix_sum[y1 - 1][x1 - 1])
    print(result_sum)
