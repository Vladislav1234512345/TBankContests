import sys
from typing import List


def calculate_painted_length(array: List[List[int]]):
    array.sort(key=lambda x: (x[0], x[1]))

    total_length = 0
    current_start, current_end = array[0]

    for start, end in array[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total_length += current_end - current_start
            current_start, current_end = start, end

    total_length += current_end - current_start

    return total_length


n = int(sys.stdin.readline())
segments = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(calculate_painted_length(array=segments))
