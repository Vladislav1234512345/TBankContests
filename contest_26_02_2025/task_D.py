import sys
from typing import List


def reversed_bubble_sort(array: List[int]) -> None:
    array_length = len(array)

    for i in range(array_length - 1):
        if array[array_length - 1 - i] < array[array_length - 2 - i]:
            array[array_length - 1 - i], array[array_length - 2 - i] = array[array_length - 2 - i], array[array_length - 1 - i]
            continue
        break


n = int(sys.stdin.readline())
heap_commands = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

current_heap = []

for heap_command in heap_commands:
    if heap_command[0] == 0:
        current_heap.append(heap_command[1])
        reversed_bubble_sort(array=current_heap)
    elif heap_command[0] == 1:
        print(current_heap.pop())