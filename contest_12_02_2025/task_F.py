import sys

def merge(arr: list[int], left: int, mid: int, right: int) -> int:
    inversions_count = 0
    n1 = mid - left + 1
    n2 = right - mid

    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(n1):
        left_array[i] = arr[left + i]
    for j in range(n2):
        right_array[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            inversions_count += len(left_array) - i
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_array[j]
        j += 1
        k += 1

    return inversions_count


def merge_sort(arr: list[int], left: int, right: int) -> int:
    inversions_count = 0
    if left < right:
        mid = left + (right - left) // 2

        inversions_count += merge_sort(arr=arr, left=left, right=mid)
        inversions_count += merge_sort(arr=arr, left=mid + 1, right=right)
        inversions_count += merge(arr=arr, left=left, mid=mid, right=right)

    return inversions_count


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    print(merge_sort(arr=numbers, left=0, right=n-1))
    print(*numbers)
