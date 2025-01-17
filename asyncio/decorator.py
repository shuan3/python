import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper
