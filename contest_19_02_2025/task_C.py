import sys


def is_operator(symbol: str) -> bool:
    if symbol in "+-*":
        return True

    return False


postfix_record = list(map(str, sys.stdin.readline().split()))

stack = []

pivot = -1


for postfix_symbol in postfix_record:
    if postfix_symbol.isdigit():
        pivot += 1
        if pivot < len(stack):
            stack[pivot] = postfix_symbol
        else:
            stack.append(postfix_symbol)
    elif is_operator(postfix_symbol):
        pivot -= 1
        stack[pivot] = str(eval(stack[pivot] + postfix_symbol + stack[pivot + 1]))

print(stack[0])