#우선순위 높은 순서대로
#priority scheduling
import create_task
import time
import copy

def get_importance(args):
    return int(args[0])


tasks = create_task.task(10)
tasks.sort(key = get_importance, reverse = True)
temp = copy.deepcopy(tasks)



for s in tasks:
    time.sleep(int(s[1] / 10))
    print(f"Task completed: {s[0]} {int(s[1] / 10)}s")

    temp.remove(s)
    print(f"Remained tasks: {temp}")