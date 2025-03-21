import sys

def count_less_equal(length: int, searched_number):
    count = 0
    for i in range(1, length + 1):
        count += min(length, searched_number // i)
    return count


def find_k_count_number(length: int, searched_number: int):
    left, right = 1, length * length
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(length=length, searched_number=mid) < searched_number:
            left = mid + 1
        else:
            right = mid
    return left


n, k = map(int, sys.stdin.readline().split())
result = find_k_count_number(length=n, searched_number=k)
print(result)