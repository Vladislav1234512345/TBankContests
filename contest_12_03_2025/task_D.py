import sys


def min_shift(text: str) -> str:
    text_length = len(text)
    min_shift_index = 0
    current_string = text + text

    for i in range(1, text_length):
        if current_string[i:i + text_length] < current_string[min_shift_index:min_shift_index + text_length]:
            min_shift_index = i
    return current_string[min_shift_index:min_shift_index + text_length]


s = str(sys.stdin.readline().strip())

print(min_shift(text=s))

