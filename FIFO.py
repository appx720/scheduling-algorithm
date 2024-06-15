#순서대로 처리
#first in first out
import create_task
import time
import copy

tasks = create_task.task(10)
remained_copy = copy.deepcopy(tasks)


for s in tasks:
    time.sleep(int(s[1] / 10))
    print(f"Task completed: {s[0]} {int(s[1] / 10)}s")

    remained_copy.remove(s)
    print(f"Remained tasks: {remained_copy}")
