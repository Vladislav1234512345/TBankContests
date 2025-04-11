import sys


n = int(sys.stdin.readline())

safe_stacks_list = [-1] * (n + 1)

safe_stacks_list[0] = 1
safe_stacks_list[1] = 3

for i in range(2, n + 1):
    safe_stacks_list[i] = 2 * (safe_stacks_list[i - 1] + safe_stacks_list[i - 2])

print(safe_stacks_list[n])