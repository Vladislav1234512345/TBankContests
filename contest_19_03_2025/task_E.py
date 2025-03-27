import heapq
import sys


def minimal_number_digits_sum(number: int) -> int:
    remainders = [sys.maxsize] * number

    sums_and_remainders_heap = ([(i, i) for i in range(1, min(10, number))])
    heapq.heapify(sums_and_remainders_heap)
    while sums_and_remainders_heap:
        heap_sum, heap_remainder = heapq.heappop(sums_and_remainders_heap)
        heap_remainder *= 10
        for i in range(10):
            current_remainder = (heap_remainder + i) % number
            if remainders[current_remainder] <= heap_sum + i:
                continue
            remainders[current_remainder] = heap_sum + i
            heapq.heappush(sums_and_remainders_heap, (heap_sum + i, current_remainder))

    return remainders[0]


k = int(sys.stdin.readline())
print(minimal_number_digits_sum(number=k))
