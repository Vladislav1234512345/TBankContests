import sys


def get_last_empty_element(array: list[int], length: int) -> int:
    for i in range(length):
        if array[length - 1 - i] == 0:
            return length - 1 - i

    return -1


def get_iterations_count_from_bubble_sorting_list(array: list[int], positions: list[int], length: int) -> list[int]:
    iterations_count_list = [0] * (length + 1)

    pivot = length - 1
    right_count = 0
    iterations_count_list[0] = 1
    for i in range(n):
        array[positions[i] - 1] = 1
        if positions[i] - 1 == pivot:
            pivot = get_last_empty_element(array=array, length=pivot)
            right_count += positions[i] - 1 - pivot

            if pivot == -1:
                iterations_count_list[i + 1] = i + 2 - right_count
                break

        iterations_count_list[i + 1] = i + 2 - right_count

    return iterations_count_list


n = int(sys.stdin.readline())
positions_array = list(map(int, sys.stdin.readline().split()))

result_array = [0] * n

print(*get_iterations_count_from_bubble_sorting_list(array=result_array, positions=positions_array, length=n))
