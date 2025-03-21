import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

prefix_sum = [0] * (n + 1)
prefix_hor = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]
    prefix_hor[i] = prefix_hor[i - 1] ^ array[i - 1]

for i in range(m):
    if queries[i][0] == 1:
        print(prefix_sum[queries[i][2]] - prefix_sum[queries[i][1] - 1])
    elif queries[i][0] == 2:
        print(prefix_hor[queries[i][2]] ^ prefix_hor[queries[i][1] - 1])
