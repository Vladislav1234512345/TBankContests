import sys


operations_count = int(sys.stdin.readline())

operations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(operations_count)]

stack = []

for operation in operations:
    if operation[0] == 1:
        stack.append(operation[1])
    elif operation[0] == 2:
        stack.pop()
    else:
        print(min(stack))
