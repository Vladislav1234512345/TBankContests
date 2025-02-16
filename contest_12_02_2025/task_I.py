import sys

n = int(sys.stdin.readline())
positions_array = list(map(int, sys.stdin.readline().split()))


def get_bubble_sort_loops_count(array: list[int]) -> int:
    bubble_sort_loops_count = 0

    for i in range(n):
        had_swaps = False
        pivot = None
        for j in range(n):
            if pivot is not None:
                if j < n - 1 and array[j + 1] == 1:
                    array[pivot] = 0
                    array[j] = 1
                    had_swaps = True
                if j == n - 1:
                    array[pivot] = 0
                    array[j] = 1
                    had_swaps = True
            else:
                if array[j] == 1:
                    pivot = j

        bubble_sort_loops_count += 1
        if not had_swaps:
            break

    return bubble_sort_loops_count


binary_array = [0] * n
result_array = [0] * (n + 1)

result_array[0] = get_bubble_sort_loops_count(array=binary_array)

for i in range(n):
    binary_array[positions_array[i] - 1] = 1
    result_array[i + 1] = get_bubble_sort_loops_count(array=[*binary_array])

print(*result_array)
