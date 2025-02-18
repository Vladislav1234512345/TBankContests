def generate_anti_quicksort_test_array(length: int):
    array = list(range(1, length + 1))
    for i in range(1, length):
        array[i], array[i//2] = array[i//2], array[i]

    return array

n = int(input())
anti_quicksort_test_array = generate_anti_quicksort_test_array(length=n)

print(*anti_quicksort_test_array)
