import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(r"https://asyncio.ru/zadachi/4/img/1659376269184872685.jpg") as response:
            print(response.headers)
           
asyncio.run(main())