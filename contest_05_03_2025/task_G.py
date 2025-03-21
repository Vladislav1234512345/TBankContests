import sys


def time_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    return hours * 3600 + minutes * 60 + seconds


n = int(sys.stdin.readline())
tills_array = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

tills_events = []

for i in range(n):
    h1, m1, s1, h2, m2, s2 = tills_array[i]
    open_time = time_to_seconds(hours=h1, minutes=m1, seconds=s1)
    close_time = time_to_seconds(hours=h2, minutes=m2, seconds=s2)

    if open_time == close_time:
        tills_events.append((0, 1))
        tills_events.append((86400, -1))
    elif open_time < close_time:
        tills_events.append((open_time, 1))
        tills_events.append((close_time, -1))
    else:
        tills_events.append((open_time, 1))
        tills_events.append((86400, -1))
        tills_events.append((0, 1))
        tills_events.append((close_time, -1))

tills_events.sort()

current_events_sum = 0
last_time = 0
general_time = 0

for time, event in tills_events:
    if current_events_sum == n:
        general_time += time - last_time

    current_events_sum += event
    last_time = time

print(general_time)
