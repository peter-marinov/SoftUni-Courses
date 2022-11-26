from time import time


def track(func_ref):
    def wrapper(*args):
        start = time()
        result = func_ref(*args)
        end = time()
        elapsed_time = end - start
        print(elapsed_time)
        return result

    return wrapper

@track
def magic(n):
    arr = []
    for num in range(n):
        arr.append(num)

    return arr

print(magic(100000))

