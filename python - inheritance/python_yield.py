# from multiprocessing import Pool

# def data_generator():
#     for i in range(1000):
#         yield i

# def process_data(data):
#     # Your processing logic here
#     return data

# if __name__ == "__main__":
#     with Pool() as pool:
#         results = pool.map(process_data, data_generator())
#         print(results)

import time


def print_run():
    print(1)


def print_run2():
    print(2)


def yield_run():
    yield print_run()
    print("done1")
    time.sleep(180)
    yield print_run2()
    print("done2")


for i in yield_run():
    print(i)

yield_run()
print("Done")
# & d:/Github/test/luigienv/Scripts/python.exe "d:/Github/test/python - inheritance/python_yield.py"
