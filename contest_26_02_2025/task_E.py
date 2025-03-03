from typing import List


def heapify(array: List[int], length: int, index: int):
    largest = index

    left = 2 * index + 1

    right = 2 * index + 2

    if left < length and array[left] > array[largest]:
        largest = left

    if right < length and array[right] > array[largest]:
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]

        heapify(array, length, largest)


def heap_sort(array: List[int], length: int):
    for i in range(length // 2 - 1, -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        array[0], array[i] = array[i], array[0]

        heapify(array, i, 0)


n = int(input())
current_array = list(map(int, input().split()))

heap_sort(array=current_array, length=n)

print(*current_array)
