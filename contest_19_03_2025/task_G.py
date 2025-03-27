import sys
import heapq
from collections import defaultdict
from typing import List, Any


def bfs_max_distance(node: int, towns_count: int, graph: defaultdict[Any, List]) -> int:
    distances = [sys.maxsize] * (towns_count + 1)
    distances[node] = 0

    towns = [(0, node)]

    while towns:
        current_distance, current_town = heapq.heappop(towns)
        if current_distance > distances[current_town]:
            continue

        for neighbour_town, neighbour_weight in graph[current_town]:
            new_distance = current_distance + neighbour_weight
            if new_distance < distances[neighbour_town]:
                distances[neighbour_town] = new_distance
                heapq.heappush(towns, (new_distance, neighbour_town))

    return max(distances[1:])


n, m = map(int, sys.stdin.readline().split())

roads_dict = defaultdict(list)


for _ in range(m):
    from_town, to_town, weight = map(int, sys.stdin.readline().split())
    roads_dict[from_town].append((to_town, weight))
    roads_dict[to_town].append((from_town, weight))


min_distance = sys.maxsize
best_town = 1

for town in range(1, n + 1):
    current_max_distance = bfs_max_distance(node=town, towns_count=n, graph=roads_dict)
    if current_max_distance < min_distance:
        min_distance = current_max_distance
        best_town = town

print(best_town)
