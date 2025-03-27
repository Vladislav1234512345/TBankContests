import sys
from typing import List


def dfs(node: int, graph: List[List], used_nodes: List[int]):
    if used_nodes[node - 1] == 1:
        return True
    elif used_nodes[node - 1] == 2:
        return False

    used_nodes[node - 1] = 1

    for child in graph[node - 1]:
        if dfs(child, graph=graph, used_nodes=used_nodes):
            return True

    used_nodes[node - 1] = 2

    return False


n, m = map(int, sys.stdin.readline().split())
connections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]


graph_list = [[] for _ in range(n)]
used_nodes_list = [0] * n

for u, v in connections:
    graph_list[u - 1].append(v)

is_cycled = 0

for node in range(1, n + 1):
    if used_nodes_list[node - 1] == 0:
        if dfs(node=node, graph=graph_list, used_nodes=used_nodes_list):
            is_cycled = 1

print(is_cycled)
