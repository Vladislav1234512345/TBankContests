import sys

n, c = map(int, sys.stdin.readline().split())
tasks_array = []

for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    tasks_array.append((s, t + s, i + 1))

tasks_array.sort(key=lambda x: x[1])
end = 0
total_points = 0
decided_tasks = []

for start_time, finish_time, task_id in tasks_array:
    if end <= start_time:
        total_points += c
        decided_tasks.append(task_id)
        end = finish_time

decided_tasks.sort()

print(total_points)
print(len(decided_tasks))
print(*decided_tasks)