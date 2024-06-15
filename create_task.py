import random

def get_weight():
    weight = []

    for i in range(10):
        weight.append(0.03)

    for i in range(40):
        weight.append(0.01)

    for i in range(50):
        weight.append(0.006)

    return weight


def task(count = 1):
    tasks = []
    weight = get_weight()

    for i in range(count):
        importance = random.choices(range(1, 101), weights = weight)[0]
        time = random.choices(range(1, 101), weights = weight)[0]
        tasks.append([importance, time])

    return tasks