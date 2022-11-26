from time import time


def exec_time(func_ref):
    def wrapper(start, end):
        start_time = time()
        result = func_ref(start, end)
        end_time = time()
        total_time_needed = end_time - start_time
        return total_time_needed

    return wrapper

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))