from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

max_length = 0

P = 31
MOD = 10 ** 9 + 7

def compute_hashes(arr, length):
    hashes = []
    freq = defaultdict(int)
    current_hash = 0

    for i in range(length):
        freq[arr[i]] += 1
        current_hash = (current_hash + freq[arr[i]] * pow(P, arr[i], MOD)) % MOD
    hashes.append(current_hash)

    for i in range(length, len(arr)):
        freq[arr[i - length]] -= 1
        current_hash = (current_hash - (freq[arr[i - length]] + 1) * pow(P, arr[i - length], MOD)) % MOD
        if freq[arr[i - length]] == 0:
            del freq[arr[i - length]]

        freq[arr[i]] += 1
        current_hash = (current_hash + freq[arr[i]] * pow(P, arr[i], MOD)) % MOD

        hashes.append(current_hash)

    return hashes

for length in range(1, min(n, m) + 1):
    hash_a = set(compute_hashes(a, length))
    hash_b = set(compute_hashes(b, length))

    if hash_a & hash_b:
        max_length = length

print(max_length)