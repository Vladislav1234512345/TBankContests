import sys


def count_cyclic_shifts(first_string: str, second_string: str) -> int:
    m = len(second_string)
    n = len(first_string)

    if m > n:
        return 0

    double_b_string = second_string + second_string
    cyclic_hashes = set()

    p = 31
    mod = 10 ** 9 + 9

    power = [1] * (m + 1)
    for i in range(1, m + 1):
        power[i] = (power[i - 1] * p) % mod

    current_hash = 0
    for i in range(m):
        current_hash = (current_hash * p + ord(double_b_string[i])) % mod
    cyclic_hashes.add(current_hash)

    for i in range(m, len(double_b_string)):
        current_hash = (current_hash - ord(double_b_string[i - m]) * power[m - 1] % mod + mod) % mod
        current_hash = (current_hash * p + ord(double_b_string[i])) % mod
        cyclic_hashes.add(current_hash)

    result = 0
    current_hash = 0

    for i in range(m):
        current_hash = (current_hash * p + ord(first_string[i])) % mod

    if current_hash in cyclic_hashes:
        result += 1

    for i in range(m, n):
        current_hash = (current_hash - ord(first_string[i - m]) * power[m - 1] % mod + mod) % mod
        current_hash = (current_hash * p + ord(first_string[i])) % mod

        if current_hash in cyclic_hashes:
            result += 1

    return result


a = str(sys.stdin.readline().strip())
b = str(sys.stdin.readline().strip())

print(count_cyclic_shifts(a, b))
