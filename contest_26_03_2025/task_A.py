import sys
from typing import List
import heapq


def min_stairs_up_dijkstra(graph: List[List[List[int]]], start: int, length: int) -> int:
    distances = [sys.maxsize] * length
    distances[start] = 0

    stairs_heap = [(0, start)]

    while stairs_heap:
        current_cost, current_stair = heapq.heappop(stairs_heap)

        if current_cost > distances[current_stair]:
            continue

        for neighbour_stair, neighbour_cost in graph[current_stair]:
            new_cost = current_cost + neighbour_cost
            if new_cost < distances[neighbour_stair]:
                distances[neighbour_stair] = new_cost
                heapq.heappush(stairs_heap, (new_cost, neighbour_stair))

    return distances[-1]


n = int(sys.stdin.readline())
stairs = list(map(int, sys.stdin.readline().split()))

stairs_graph = [[] for _ in range(n + 1)]


for i in range(n + 1):
    if i < n:
        stairs_graph[i].append([i + 1, stairs[i]])
        if i < n - 1:
            stairs_graph[i].append([i + 2, stairs[i + 1]])


print(stairs_graph)


print(min_stairs_up_dijkstra(graph=stairs_graph, start=0, length=n + 1))
