import sys


n = int(sys.stdin.readline())
positions_array = list(map(int, sys.stdin.readline().split()))


def get_bubble_sort_loops_count(array: list[int]) -> int:
    prev_one_digit_index = None
    sub_arrays = []
    all_numbers_same = True
    for i in range(n):
        if array[n - 1] != array[n - 1 - i]:
            all_numbers_same = False
        if all_numbers_same and array[n - 1] == 1:
            continue
        if array[n - 1 - i] == 1:
            if prev_one_digit_index is not None:
                sub_arrays.append(array[n - 1 - i:prev_one_digit_index + 1])
            prev_one_digit_index = n - 1 - i

    if all_numbers_same:
        return 1
    sub_arrays.append(array[0: prev_one_digit_index + 1])

    sub_arrays_length = len(sub_arrays)

    return sub_arrays_length + 1


binary_array = [0] * n
result_array = [1] * (n + 1)

result_array[0] = 1

for index in range(n):
    if index == n - 1:
        continue
    binary_array[positions_array[index] - 1] = 1
    result_array[index + 1] = get_bubble_sort_loops_count(array=binary_array)


print(*result_array)
