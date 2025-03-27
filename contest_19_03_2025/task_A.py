import sys
from collections import defaultdict
from typing import List, Any


def iterative_dfs(node: int, graph: defaultdict[Any, List], visited: List[bool]):
    stack = [node]
    current_component = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            current_component.append(node)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return sorted(current_component)


n, m = map(int, sys.stdin.readline().split())

graph_list = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph_list[u].append(v)
    graph_list[v].append(u)

visited_nodes = [False] * (n + 1)
components = []


for current_node in range(1, n + 1):
    if not visited_nodes[current_node]:
        components.append(iterative_dfs(node=current_node, graph=graph_list, visited=visited_nodes))

print(len(components))
for component in components:
    print(len(component))
    print(*component)
