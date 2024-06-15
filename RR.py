#조금씩 쪼개서 처리
#Round Robin
import create_task
import random
import time
import copy

def sort_task(tasks):
    i = 0
    t = []

    for s in tasks:
        for i in range(s[1] // 1):
            t.append([s[0], 1])

        i += 1

    tasks.clear()
    tasks.extend(t)
    random.shuffle(tasks)



tasks = create_task.task(10)
sort_task(tasks)
temp = copy.deepcopy(tasks)



for s in tasks:
    time.sleep(s[1] / 10)
    print(f"Task completed: {s[0]} {s[1] / 10}s")

    temp.remove(s)
    #print(f"Remained tasks: {temp}") #출력값이 너무 많아서 주석처리