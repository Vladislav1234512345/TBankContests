import sys


n = int(sys.stdin.readline())
carriages_array = list(map(int, sys.stdin.readline().split()))[::-1]

searching_carriage_number = 1

temporary_array = []

formed_carriages_array = []

total_carriages_moves = []


while True:
    if carriages_array:

        from_carriages_count = 0
        to_carriages_count = 0

        while True:
            from_carriages_count += 1
            last_carriage = carriages_array.pop()
            temporary_array.append(last_carriage)
            if last_carriage == searching_carriage_number or not carriages_array:
                break

        while True:
            if temporary_array:
                if temporary_array[-1] == searching_carriage_number:
                    to_carriages_count += 1
                    formed_carriages_array.append(temporary_array.pop())
                    searching_carriage_number += 1
                    continue
            break
        total_carriages_moves.append((1, from_carriages_count))
        total_carriages_moves.append((2, to_carriages_count))
    else:
        break


if len(formed_carriages_array) == n:
    print(len(total_carriages_moves))
    for action, carriage_number in total_carriages_moves:
        print(action, carriage_number)
else:
    print(0)
