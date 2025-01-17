import concurrent.futures
from decorator import timer
import time


@timer
def worker():
    print("Worker thread running")
    time.sleep(2)


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)

pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
