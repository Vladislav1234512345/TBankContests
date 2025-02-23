import sys


def min_tuple_first_element(array: list[tuple[int, int]]) -> int:
    print(array)
    min_value = sys.maxsize
    for el in array:
        min_value = min(min_value, el[0])

    return min_value


def get_min_values_from_windows(array: list[int], length: int, step: int) -> list[int]:
    windows_values_stack = []
    for i in range(length):
        if i % step == 0:
            if windows_values_stack:
                windows_values_stack.append((array[i], min(array[i], min_tuple_first_element(array=windows_values_stack[-step:]))))
            else:
                windows_values_stack.append((array[i], array[i]))
        else:
            windows_values_stack.append((array[i], min(array[i], windows_values_stack[-1][1])))

    print(windows_values_stack)
    return []


# n, k = list(map(int, sys.stdin.readline().split()))
# windows_array = list(map(int, sys.stdin.readline().split()))

n, k = 7, 3
windows_array = [1, 3, 2, 4, 5, 3, 1]

print(*get_min_values_from_windows(array=windows_array, length=n, step=k))
