import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
max_side = 0
max_i, max_j = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            if dp[i][j] >= max_side:
                max_side = dp[i][j]
                max_i, max_j = i, j

top_left_i = max_i - max_side + 1
top_left_j = max_j - max_side + 1

print(max_side)
print(top_left_i + 1, top_left_j + 1)
