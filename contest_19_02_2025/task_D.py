import sys


def get_destroyed_balls(array: list[int], length: int) -> None:
    balls_stack = []
    destroyed_balls_count = 0
    for i in range(length):

        balls_stack.append(array[i])

        if len(balls_stack) > 2 and balls_stack[-1] == balls_stack[-2] == balls_stack[-3]:
            if i == length - 1 or array[i + 1] != balls_stack[-1]:
                while True:
                    if balls_stack:
                        if array[i] == balls_stack[-1]:
                            destroyed_balls_count += 1
                            balls_stack.pop()
                            continue
                    break
    return destroyed_balls_count


n = int(sys.stdin.readline())
balls_array = list(map(int, sys.stdin.readline().split()))

print(get_destroyed_balls(array=balls_array, length=n))
