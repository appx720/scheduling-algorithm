#시간 순대로
#shortest-job-first
import create_task
import time
import copy

def get_time(args):
    return int(args[1])

tasks = create_task.task(10)
tasks.sort(key = get_time)
temp = copy.deepcopy(tasks)



for s in tasks:
    time.sleep(int(s[1] / 10))
    print(f"Task completed: {s[0]} {int(s[1] / 10)}s")

    temp.remove(s)
    print(f"Remained tasks: {temp}")