import sys


def damerau_levenshtein_distance(first_string: str, second_string: str):
    n, m = len(first_string), len(second_string)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1
                )

            if i > 1 and j > 1 and first_string[i - 1] == second_string[j - 2] and first_string[i - 2] == second_string[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[n][m]


s1 = str(sys.stdin.readline().strip())
s2 = str(sys.stdin.readline().strip())

result = damerau_levenshtein_distance(s1, s2)

print(result)
