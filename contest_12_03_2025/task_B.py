from typing import List
import sys


def kmp_preprocess(pattern) -> List[int]:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern) -> List[int]:
    n = len(text)
    m = len(pattern)
    lps = kmp_preprocess(pattern)
    i = 0
    j = 0
    occurrences = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


s = str(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
queries = [str(sys.stdin.readline().strip()) for _ in range(q)]

results = []

for query in queries:
    current_occurrences = kmp_search(s, query)
    count = len(current_occurrences)
    results.append((count, current_occurrences))

for count, indices in results:
    if count > 0:
        print(count, *indices)
    else:
        print(0)
