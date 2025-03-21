import sys
from typing import List

def manacher_odd(text: str) -> List[int]:
    text = '$' + text + '^'
    n = len(text)
    res = [0] * n
    l = 0
    r = 0
    for i in range(1, n - 1):
        res[i] = max(0, min(r - i, res[l + (r - i)]))
        while text[i - res[i]] == text[i + res[i]]:
            res[i] += 1
        if i + res[i] > r:
            l = i - res[i]
            r = i + res[i]
    return res[1:-1]


def substrings_are_palindromes_count(text: str) -> int:
    result_string = manacher_odd('#' + '#'.join(text) + '#')[1:-1]
    substrings_count = 0
    for x in result_string[::2]:
        substrings_count += x // 2
    for x in result_string[1::2]:
        substrings_count += x // 2

    return substrings_count


s = str(sys.stdin.readline().strip())

print(substrings_are_palindromes_count(s))