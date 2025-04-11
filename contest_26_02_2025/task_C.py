import sys
from typing import List


def find_lca_using_dfs(a: int, b: int, graph: List[List[int]], length: int) -> int:
    visited_a = [False] * length
    visited_b = [False] * length

    stack_a = [a]
    stack_b = [b]

    while stack_a and stack_b:
        node_a = stack_a.pop()
        node_b = stack_b.pop()

        if not visited_a[node_a]:
            for neighbour_a in graph[node_a]:
                if not visited_a[neighbour_a]:
                    stack_a.append(neighbour_a)

        if not visited_b[node_b]:
            for neighbour_b in graph[node_b]:
                if not visited_b[neighbour_b]:
                    stack_b.append(neighbour_b)

        visited_a[node_a] = True
        visited_b[node_b] = True

        if visited_a[node_a] and visited_b[node_a]:
            return node_a

        if visited_a[node_b] and visited_b[node_b]:
            return node_b

    while stack_a:
        node_a = stack_a.pop()

        if not visited_a[node_a]:
            for neighbour_a in graph[node_a]:
                if not visited_a[neighbour_a]:
                    stack_a.append(neighbour_a)

        visited_a[node_a] = True

        if visited_a[node_a] and visited_b[node_a]:
            return node_a

    while stack_b:
        node_b = stack_b.pop()

        if not visited_b[node_b]:
            for neighbour_b in graph[node_b]:
                if not visited_b[neighbour_b]:
                    stack_b.append(neighbour_b)

        visited_b[node_b] = True

        if visited_a[node_b] and visited_b[node_b]:
            return node_b


n = int(sys.stdin.readline())
ancestors = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

tree_graph = [[] for _ in range(n)]

peek_count = 0

for ancestor in ancestors:
    peek_count += 1
    tree_graph[peek_count].append(ancestor)

for current_a, current_b in queries:
    print(find_lca_using_dfs(a=current_a, b=current_b, graph=tree_graph, length=n))
