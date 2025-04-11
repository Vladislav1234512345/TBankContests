import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))

dp = [-sys.maxsize] * n
dp[0] = 0
prev = [-1] * n

coins.append(0)

coins_deque = deque()
coins_deque.append(0)

for i in range(1, n):

    while coins_deque and coins_deque[0] < i - k:
        coins_deque.popleft()

    if coins_deque:
        dp[i] = dp[coins_deque[0]] + coins[i - 1]
        prev[i] = coins_deque[0]

    while coins_deque and dp[i] >= dp[coins_deque[-1]]:
        coins_deque.pop()

    coins_deque.append(i)

print(dp[-1])

indexes = []

cur_index = n - 1
while cur_index > 0:
    indexes.append(prev[cur_index] + 1)
    cur_index = prev[cur_index]

print(len(indexes))

indexes.reverse()
indexes.append(n)

print(*indexes)