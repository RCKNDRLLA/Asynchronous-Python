import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

def io_task(n):
    time.sleep(1)  # имитация I/O
    return n

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=10_000) as executor:
    results = list(executor.map(io_task, range(10_000)))
print(f"10_000 потоков: {time.perf_counter() - start:.2f} сек")



async def async_io_task(n):
    await asyncio.sleep(1)  # имитация I/O
    return n

async def main():
    tasks = [asyncio.create_task(async_io_task(i)) for i in range(10_000)]
    results = await asyncio.gather(*tasks)

start = time.perf_counter()
asyncio.run(main())
print(f"10_000 корутин: {time.perf_counter() - start:.2f} сек")