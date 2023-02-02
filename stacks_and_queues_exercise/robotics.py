from collections import deque
from math import floor


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_seconds(time):
    hours, minutes, seconds = [int(x) for x in time.split(':')]
    return (hours * 60 * 60) + (minutes * 60) + seconds


def get_time(seconds):
    seconds %= 60 * 60 * 24
    hours = seconds // (60 * 60)
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = []
robots_input = input().split(";")
for robot in robots_input:
    name, processing_time = robot.split("-")
    robots.append(Robot(name, int(processing_time)))

start_time = input()
time_seconds = get_seconds(start_time)

items = deque()
item = input()

while not item == "End":
    items.append(item)
    item = input()

while items:
    current_item = items[0]
    time_seconds += 1
    found_robot = False
    for robot in robots:
        if time_seconds >= robot.busy_until:
            robot.busy_until = time_seconds + robot.processing_time
            found_robot = True
            print(f"{robot.name} - {current_item} [{get_time(time_seconds)}]")
            break

    if found_robot:
        items.popleft()
    else:
        items.append(items.popleft())

