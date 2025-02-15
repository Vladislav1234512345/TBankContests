n, k = map(int, input().split())
sorted_array = list(map(int, input().split()))
searched_numbers_array = list(map(int, input().split()))



def binary_search(array: list[int], low: int, high: int, searched_number: int) -> bool:
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > searched_number:
            high = mid - 1
        elif array[mid] < searched_number:
            low = mid + 1
        else:
            return True

    return False


for number in searched_numbers_array:
    if binary_search(array=sorted_array, low=0, high=n - 1, searched_number=number):
        print("YES")
    else:
        print("NO")
