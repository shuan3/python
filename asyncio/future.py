import time
import asyncio


async def set_future_result(future, value):
    await asyncio.sleep(3)
    future.set_result(value)
    print(f"Setting the future result to : {value}")


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    asyncio.create_task(set_future_result(future, "future result is ready"))
    result = await future
    print(f"Received result from the future: {result}")


# wait for a set event for the next code run.
start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
# asyncio.run(main())
