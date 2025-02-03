import functools

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper


# @timer
# @functools.cache
# def factorial(n):
#     return n * factorial(n-1) if n else 1


# print(factorial(10))


@timer
@functools.cache
def slow_function(n):
    print(f"Calculating {n}...")
    time.sleep(2)  # Simulate a slow operation
    return n * 2


# First call takes time
print(slow_function(10))  # Output: 20 (after a 2-second delay)

# Second call with the same argument is instant
print(slow_function(10))  # Output: 20 (cached result, no delay)
