from collections import deque


class ConcertQueue:
    def __init__(self):
        self.queue = deque()
        self.passed_count = 0
        self.persons_map = {}

    def add_person(self, person_id: int):
        self.queue.append(person_id)
        self.persons_map[person_id] = len(self.queue) - 1 + self.passed_count

    def remove_first_person(self):
        if self.queue:
            first_person = self.queue.popleft()
            del self.persons_map[first_person]
            self.passed_count += 1

    def remove_last_person(self):
        if self.queue:
            last_person = self.queue.pop()
            del self.persons_map[last_person]

    def get_persons_count_before_person_id(self, person_id):
        print(self.persons_map[person_id] - self.passed_count)

    def get_first_person(self):
        if self.queue:
            print(self.queue[0])


def make_concert_events(events: list[tuple[int, ...]]):
    concert_queue = ConcertQueue()

    for event in events:
        if event[0] == 1:
            concert_queue.add_person(event[1])
        elif event[0] == 2:
            concert_queue.remove_first_person()
        elif event[0] == 3:
            concert_queue.remove_last_person()
        elif event[0] == 4:
            concert_queue.get_persons_count_before_person_id(event[1])
        elif event[0] == 5:
            concert_queue.get_first_person()


n = int(input())
events_array = [tuple(map(int, input().split())) for _ in range(n)]

make_concert_events(events=events_array)