import sys


def max_valid_bracket_sequence(brackets: str):
    n = len(brackets)
    dp = [[0] * n for _ in range(n)]
    parents = [[None] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if (brackets[i] == '(' and brackets[j] == ')') or \
               (brackets[i] == '[' and brackets[j] == ']') or \
               (brackets[i] == '{' and brackets[j] == '}'):
                dp[i][j] = dp[i + 1][j - 1] + 2
                parents[i][j] = ('pair', i + 1, j - 1)

            for k in range(i, j):
                if dp[i][j] < dp[i][k] + dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    parents[i][j] = ('split', k)


    def reconstruct(left, right):
        if left > right:
            return ""
        if parents[left][right] is None:
            return ""
        parent_data = parents[left][right]
        if parent_data[0] == 'pair':
            return brackets[left] + reconstruct(parent_data[1], parent_data[2]) + brackets[right]
        elif parent_data[0] == 'split':
            return reconstruct(left, parent_data[1]) + reconstruct(parent_data[1] + 1, right)

    return reconstruct(left=0, right=n - 1)


brackets_str = str(sys.stdin.readline().strip())
print(max_valid_bracket_sequence(brackets=brackets_str))


