import sys
from collections import defaultdict, deque
from typing import List, Any


def bfs(source: str, product: str, graph: defaultdict[Any, List[str]], visited: defaultdict[Any, bool]) -> int:
    substances_queue = deque([(source, 0)])
    visited[source] = True
    tree_height = 0
    while substances_queue:
        tree_height += 1
        current_substance, steps = substances_queue.popleft()

        for current_product in graph[current_substance]:

            if not visited[current_product]:
                visited[current_product] = True
                substances_queue.append((current_product, steps + 1))
                if current_product == product:
                    return steps + 1

    return -1


m = int(sys.stdin.readline())

graph_dict = defaultdict(list)

for _ in range(m):
    source_substance, product_substance = map(str, sys.stdin.readline().strip().split(' -> '))
    graph_dict[source_substance].append(product_substance)
    if graph_dict.get(product_substance) is None:
        graph_dict[product_substance] = []

visited_nodes = defaultdict(lambda: False)

source_substance = str(sys.stdin.readline().strip())
product_substance = str(sys.stdin.readline().strip())

print(bfs(source=source_substance, product=product_substance, graph=graph_dict, visited=visited_nodes))
