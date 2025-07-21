import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def scan_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                number_tag = soup.find('p', {'id': 'number'})
                return number_tag.text

async def find_links(url, semaphore, prefix=''):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(prefix+url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                results = soup.find_all('a', class_='link')
                return [result['href'] for result in results]

async def main():
    semaphore = asyncio.Semaphore(75)
    async with aiohttp.ClientSession() as session:
        links_1_level = await find_links(r'https://asyncio.ru/zadachi/3/index.html', semaphore)
        links_2_level = []
        for link in links_1_level:
            links = await find_links(link, semaphore, prefix=r'https://asyncio.ru/zadachi/3/')
            links_2_level.extend(links)

        tasks = [scan_url(fr'https://asyncio.ru/zadachi/3/depth1/{link}', semaphore) for link in links_2_level]
        results = await asyncio.gather(*tasks)
        print(sum(int(result) for result in results))
        
asyncio.run(main())