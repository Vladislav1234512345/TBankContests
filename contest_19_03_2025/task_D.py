from collections import deque


def knight_moves(n, start_x, start_y, end_x, end_y):
    moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
             (1, -2), (2, -1), (1, 2), (2, 1)]

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited[start_x][start_y] = True

    parent = [[None] * (n + 1) for _ in range(n + 1)]

    while queue:
        x, y, dist = queue.popleft()

        if x == end_x and y == end_y:
            path = []
            while (x, y) != (start_x, start_y):
                path.append((x, y))
                x, y = parent[x][y]
            path.append((start_x, start_y))
            path.reverse()
            return dist, path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny, dist + 1))

    return -1, []


n = int(input())
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

distance, path = knight_moves(n, start_x, start_y, end_x, end_y)

print(distance)
for x, y in path:
    print(x, y)