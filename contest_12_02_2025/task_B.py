n, k = map(int, input().split())
sorted_array = list(map(int, input().split()))
searched_numbers_array = list(map(int, input().split()))



def binary_search(array: list[int], low: int, high: int, searched_number: int) -> int:
    min_interval = abs(array[0] - searched_number)
    result_number = array[0]
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > searched_number:
            high = mid - 1
        elif array[mid] < searched_number:
            low = mid + 1
        else:
            return array[mid]
        if mid > 0:
            if abs(array[mid - 1] - searched_number) <= min_interval:
                min_interval = abs(array[mid - 1] - searched_number)
                result_number = array[mid - 1]
        if mid < n - 1:
            if abs(array[mid + 1] - searched_number) < min_interval:
                min_interval = abs(array[mid + 1] - searched_number)
                result_number = array[mid + 1]

    return result_number



def main():
    for number in searched_numbers_array:
        print(binary_search(array=sorted_array, low=0, high=n - 1, searched_number=number))


if __name__ == "__main__":
    main()

