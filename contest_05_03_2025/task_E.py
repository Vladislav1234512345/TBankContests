import sys
from typing import List


def can_split(arr: List[int], slices_count: int, max_sum: int):
    count = 1
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            count += 1
            current_sum = num
            if count > slices_count:
                return False

    return True


def find_min_of_max_sum(arr: List[int], slices_count: int):
    left = max(arr)
    right = sum(arr)

    while left < right:
        mid = (left + right) // 2
        if can_split(arr=arr, slices_count=slices_count, max_sum=mid):
            right = mid
        else:
            left = mid + 1

    return left


n, k = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

result = find_min_of_max_sum(arr=array, slices_count=k)
print(result)
