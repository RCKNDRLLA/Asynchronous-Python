import aiohttp
import asyncio
from aiohttp.client import ClientResponse
from bs4 import BeautifulSoup

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(r'https://asyncio.ru/zadachi/1/index.html') as response:
            page_content = await response.text()
            soup = BeautifulSoup(page_content, 'html.parser')
            p_text = soup.find('p').text.strip()
            res = ''.join([code_dict[int(number)] for number in p_text])
            print(res)

asyncio.run(main())