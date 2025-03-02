from collections import deque
import sys


def get_min_values_from_windows(array: list[int], length: int, step: int) -> list[int]:
    windows_values = []
    windows_indexes_deque = deque()

    for i in range(length):

        if windows_indexes_deque and windows_indexes_deque[0] < i - step + 1:
            windows_indexes_deque.popleft()

        while windows_indexes_deque and array[windows_indexes_deque[-1]] > array[i]:
            windows_indexes_deque.pop()

        windows_indexes_deque.append(i)

        if i >= step - 1:
            windows_values.append(array[windows_indexes_deque[0]])

    return windows_values


n, k = list(map(int, sys.stdin.readline().split()))
windows_array = list(map(int, sys.stdin.readline().split()))

print(*get_min_values_from_windows(array=windows_array, length=n, step=k))
