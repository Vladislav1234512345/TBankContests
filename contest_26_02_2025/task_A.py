import sys
from collections import deque
from typing import Optional, Dict, Tuple, List


def bfs_depths(graph: Dict[int, List[int]], distances: Dict[int, Optional[int]], source: int) -> Tuple[List[int], int]:
    distances[source] = 0
    max_depth = 0
    queue = deque([source])
    depths = [0] * len(distances)
    while queue:
        current = queue.popleft()
        for peek in graph[current]:
            if distances[peek] is None:
                distances[peek] = distances[current] + 1
                queue.append(peek)
                depths[peek] = distances[current] + 1
                max_depth = max(max_depth, distances[peek])

    return depths, max_depth


def bfs_width(graph: Dict[int, List[int]], distances: Dict[int, Optional[int]], source: int) -> Tuple[int, int]:
    distances[source] = 0
    queue = deque([source])
    farthest_peek = source
    max_distance = 0

    while queue:
        current = queue.popleft()
        for peek in graph[current]:
            if distances[peek] is None:
                distances[peek] = distances[current] + 1
                queue.append(peek)

                if distances[peek] > max_distance:
                    max_distance = distances[peek]
                    farthest_peek = peek

    return farthest_peek, max_distance


n = int(sys.stdin.readline())
peeks_array = list(map(int, sys.stdin.readline().split()))

current_graph = {}
current_number = 0

for current_peek in peeks_array:
    current_number += 1
    if current_graph.get(current_peek, None) is None:
        current_graph[current_peek] = [current_number]
    else:
        current_graph[current_peek].append(current_number)
    if current_graph.get(current_number, None) is None:
        current_graph[current_number] = [current_peek]

current_distances = {node: None for node in current_graph.keys()}

farthest_peek_A, _ = bfs_width(graph=current_graph, distances=current_distances.copy(), source=0)

farthest_peek_B, diameter = bfs_width(graph=current_graph, distances=current_distances.copy(), source=farthest_peek_A)

depths_array, current_max_depth = bfs_depths(graph=current_graph, distances=current_distances.copy(), source=0)

print(current_max_depth, diameter)
print(*depths_array)
