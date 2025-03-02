import sys


def get_max_value(arr: list[int], length: int) -> int:
    prefix_sums_array = []
    previous_indexes = [-1] * length
    next_indexes = [length - 1] * length
    previous_indexes_stack = []
    next_indexes_stack = []
    for i in range(length):
        while previous_indexes_stack and arr[previous_indexes_stack[-1]] >= arr[i]:
            previous_indexes_stack.pop()
        if previous_indexes_stack and arr[previous_indexes_stack[-1]] < arr[i]:
            previous_indexes[i] = previous_indexes_stack[-1]

        while next_indexes_stack and arr[next_indexes_stack[-1]] >= arr[length - 1 - i]:
            next_indexes_stack.pop()
        if next_indexes_stack and arr[next_indexes_stack[-1]] < arr[length - 1 - i]:
            next_indexes[length - 1 - i] = next_indexes_stack[-1] - 1

        if prefix_sums_array:
            prefix_sums_array.append(prefix_sums_array[-1] + arr[i])
        else:
            prefix_sums_array.append(arr[i])

        previous_indexes_stack.append(i)
        next_indexes_stack.append(length - 1 - i)

    max_value = -sys.maxsize

    for i in range(length):
        if previous_indexes[i] != -1:
            max_value = max(max_value,
                            (prefix_sums_array[next_indexes[i]] - prefix_sums_array[previous_indexes[i]]) * arr[i])
        else:
            max_value = max(max_value, (prefix_sums_array[next_indexes[i]] * arr[i]))
    return max_value


n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

print(get_max_value(arr=array, length=n))
