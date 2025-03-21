import sys


def find_lca(u, v, parent, depth):
    # Поднимаем u и v до одного уровня
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]

    # Поднимаем оба узла до тех пор, пока они не станут равными
    while u != v:
        u = parent[u]
        v = parent[v]

    return u


n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
depth = [0] * n

results = []

for i in range(m):
    u, v = map(int, queries[i])
    lca = find_lca(u, v, parents, depth)
    results.append(lca)

print(*results)
