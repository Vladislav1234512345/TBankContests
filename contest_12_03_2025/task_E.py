import sys

p = str(sys.stdin.readline().strip())
t = str(sys.stdin.readline().strip())

P = 31
MOD = 10 ** 10 + 9

def compute_prefix_hashes(s):
    n = len(s)
    hashes = [0] * (n + 1)
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        hashes[i] = (hashes[i - 1] * P + ord(s[i - 1])) % MOD
        powers[i] = (powers[i - 1] * P) % MOD
    return hashes, powers

p_hashes, p_powers = compute_prefix_hashes(p)
t_hashes, t_powers = compute_prefix_hashes(t)

def get_hash(hashes, powers, l, r):
    return (hashes[r] - hashes[l] * powers[r - l]) % MOD

m = len(p)
n = len(t)

result = []
for i in range(n - m + 1):
    mismatch_found = False
    for j in range(m):
        if p[j] != t[i + j]:
            left_hash = get_hash(p_hashes, p_powers, 0, j)
            right_hash = get_hash(p_hashes, p_powers, j + 1, m)
            t_left_hash = get_hash(t_hashes, t_powers, i, i + j)
            t_right_hash = get_hash(t_hashes, t_powers, i + j + 1, i + m)
            if left_hash == t_left_hash and right_hash == t_right_hash:
                mismatch_found = True
                break
            else:
                mismatch_found = False
                break
    if mismatch_found or j == m - 1:
        result.append(i + 1)

print(len(result))
print(*result)