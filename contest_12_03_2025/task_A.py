import sys
from typing import Tuple, List

MOD = 10 ** 10 + 9
P = 31


def preprocess_hashes(text: str) -> Tuple[List[int], List[int]]:
    n = len(text)
    hashes = [0] * (n + 1)
    powers = [1] * (n + 1)

    for i in range(1, n + 1):
        char_value = ord(text[i - 1])
        powers[i] = (powers[i - 1] * P) % MOD

    return hashes, powers


def get_hash(hashes: List[int], powers: List[int], left: int, right: int) -> int:
    return (hashes[right] - hashes[left - 1] * powers[right - left + 1]) % MOD


s = str(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

current_hashes, current_powers = preprocess_hashes(text=s)

results = []
for a, b, c, d in queries:
    first_substring_hash = get_hash(hashes=current_hashes, powers=current_powers, left=a, right=b)
    second_substring_hash = get_hash(hashes=current_hashes, powers=current_powers, left=c, right=d)
    if first_substring_hash == second_substring_hash:
        print("Yes")
    else:
        print("No")
