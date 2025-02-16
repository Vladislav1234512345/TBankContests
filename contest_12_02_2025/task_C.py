import sys


n = int(input())


def query(number: int) -> str:
    print(number)
    sys.stdout.flush()
    return input()


low = 1
high = n


while low <= high:
    mid = low + (high - low) // 2
    response = query(number=mid)
    if response == "<":
        high = mid - 1
    elif response == ">=":
        low = mid + 1


print(f"! {high}")