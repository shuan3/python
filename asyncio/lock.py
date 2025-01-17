import time
import asyncio

# https://www.youtube.com/watch?v=Qb9s3UiMSTA
shared_resource = 0
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    async with lock:
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resource}")


async def main():

    await asyncio.gather(*[modify_shared_resource() for _ in range(5)])


# wait for a set event for the next code run.
start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
# asyncio.run(main())


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.intersection(b).union({7, 8})
result = a | b
# result=a.update(b)
print(result)
