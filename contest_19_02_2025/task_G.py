from collections import deque
import sys


n = int(sys.stdin.readline())
first_half_goblins = deque()
second_half_goblins = deque()
result_array = []
first_half_goblins_length = 0
second_half_goblins_length = 0
for i in range(n):
    query = sys.stdin.readline().split()
    if '-' == query[0]:
        result_array.append(first_half_goblins.popleft())
        first_half_goblins_length -= 1
    elif '+' == query[0]:
        second_half_goblins.append(query[-1])
        second_half_goblins_length += 1
    elif '*' == query[0]:
        second_half_goblins.appendleft(query[-1])
        second_half_goblins_length += 1
    if first_half_goblins_length < second_half_goblins_length:
        first_half_goblins.append(second_half_goblins.popleft())
        second_half_goblins_length -= 1
        first_half_goblins_length += 1

print(*result_array, sep='\n')