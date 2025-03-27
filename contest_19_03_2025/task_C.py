import sys


n, m = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
permutations = list(map(int, sys.stdin.readline().split()))

positions = [0] * (n + 1)

for index, element in enumerate(permutations):
    positions[element] = index


is_topological_sorting = True

for u, v in edges:
    if positions[u] > positions[v]:
        is_topological_sorting = False
        break

if is_topological_sorting:
    print("YES")
else:
    print("NO")