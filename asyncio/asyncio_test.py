import asyncio
import time

# Example 1
# async def fetch_data(delay):
#     print(f"Start fetching data with delay {delay}")
#     # await asyncio.sleep(delay)
#     await asyncio.sleep(delay)
#     return {"data":"Some data"}


# async def main():
#     print('Hello ...')
#     task=fetch_data(2)
#     result=await task  # the task is executed at here
#     print('... World!')


# Example 2

# async def fetch_data(id,sleep_time):
#     print(f"{id}, starting to fetch data")
#     await asyncio.sleep(sleep_time)
#     return {"id":id,"data":f"Some data from P{id}"}

# async def main():
#     print('Hello ...')
#     task1=fetch_data(1,2)
#     task2=fetch_data(2,1)
#     task3=fetch_data(3,5)
#     task4=fetch_data(4,6)

#     tasks=[task1,task2,task3,task4]
#     results=await asyncio.gather(*tasks)
#     print(results)
#     print('... World!')

# Example 3
async def fetch_data(id, sleep_time):
    print(f"{id}, starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Some data from {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 5, 6], start=1):
            tasks.append(tg.create_task(fetch_data(i, sleep_time)))
    results = [task.result() for task in tasks]
    for result in results:
        print(f"Received result {result}")


start_time = time.time()
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
# asyncio.run(main())
