import threading
import time


def print_cube(num):
    print("Cube: {}".format(num * num * num))
    time.sleep(5)


def print_square(num):
    print("Square: {}".format(num * num))
    time.sleep(5)


if __name__ == "__main__":
    start_time = time.time()
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
    print("--- %s seconds ---" % (time.time() - start_time))
