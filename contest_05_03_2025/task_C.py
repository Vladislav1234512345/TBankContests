import sys


def can_place_cows(array, length, cows_count, min_distance):
    count = 1
    last_position = array[0]

    for i in range(1, length):
        if array[i] - last_position >= min_distance:
            count += 1
            last_position = array[i]
            if count == cows_count:
                return True

    return count >= cows_count

def find_max_distance(array: list[int], length: int, cows_count: int):
    left = 1
    right = array[-1] - array[0]

    while left < right:
        mid = (left + right + 1) // 2
        if can_place_cows(array, length, cows_count, mid):
            left = mid
        else:
            right = mid - 1

    return left


n, k = list(map(int, sys.stdin.readline().split()))
stalls = list(map(int, sys.stdin.readline().split()))

result = find_max_distance(stalls, n, k)
print(result)