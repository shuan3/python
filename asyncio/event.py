import time
import asyncio


async def waiter(event):
    print("waiting for event to be set ...")
    await event.wait()
    print("event has been set and now processed")


async def setter(event):
    await asyncio.sleep(3)
    event.set()
    print("event has been set")


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


# wait for a set event for the next code run.
start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
# asyncio.run(main())
