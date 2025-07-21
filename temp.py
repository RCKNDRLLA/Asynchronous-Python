import aiohttp
import asyncio
from aiohttp.client import ClientResponse


# Колбэк-функции для обработчиков
async def scan_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                return response.status


async def main():
    semaphore = asyncio.Semaphore(10)
    tasks = [scan_url(fr'https://asyncio.ru/zadachi/5/{i}.html', semaphore) for i in range(1, 1001)]
    results = await asyncio.gather(*tasks)
    print(sum(results))

asyncio.run(main())