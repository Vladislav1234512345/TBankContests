import sys


def search_horizontal_index_and_sum(half_sum: int, low: int, high: int, columns: int) -> (int, int):
    horizontal_sum = 0
    horizontal_index = high
    horizontal_min_difference = sys.maxsize

    while low <= high:
        mid = low + (high - low) // 2
        current_row_sum = mid * columns * (mid * columns + 1) // 2

        if current_row_sum < half_sum:
            low = mid + 1
        elif current_row_sum > half_sum:
            high = mid - 1
        else:
            return mid, current_row_sum

        if abs(current_row_sum - half_sum) < horizontal_min_difference:
            horizontal_sum = current_row_sum
            horizontal_min_difference = abs(horizontal_sum - half_sum)
            horizontal_index = mid

    return horizontal_index, horizontal_sum


def search_vertical_index_and_sum(half_sum: int, low: int, high: int, rows: int, columns: int) -> (int, int):
    vertical_sum = 0
    vertical_index = high
    vertical_min_difference = sys.maxsize

    while low <= high:
        mid = low + (high - low) // 2
        main_column_sum_part = (mid - 1) * columns * (rows - 1) * rows // 2
        left_column_sum_part = (rows * (mid - 1) * mid) // 2
        current_column_sum = main_column_sum_part + left_column_sum_part

        if current_column_sum < half_sum:
            low = mid + 1
        elif current_column_sum > half_sum:
            high = mid - 1
        else:
            return mid, current_column_sum

        if abs(current_column_sum - half_sum) < vertical_min_difference:
            vertical_sum = current_column_sum
            vertical_min_difference = abs(vertical_sum - half_sum)
            vertical_index = mid

    return vertical_index, vertical_sum


def split_table(rows: int, columns: int) -> str:
    half_sum = rows * columns * (rows * columns + 1) // 4

    vertical_index, vertical_sum = search_vertical_index_and_sum(half_sum=half_sum, low=0, high=columns, rows=rows,
                                                                 columns=columns)

    horizontal_index, horizontal_sum = search_horizontal_index_and_sum(half_sum=half_sum, low=0, high=rows,
                                                                       columns=columns)

    if abs(vertical_sum - half_sum) <= abs(horizontal_sum - half_sum):
        return f"V {vertical_index}"
    else:
        return f"H {horizontal_index + 1}"


queries_count = int(sys.stdin.readline())

tables = [tuple(map(int, sys.stdin.readline().split())) for _ in range(queries_count)]

for table in tables:
    print(split_table(rows=table[0], columns=table[1]))
