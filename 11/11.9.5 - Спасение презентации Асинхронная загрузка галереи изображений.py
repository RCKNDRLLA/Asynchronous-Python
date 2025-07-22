# Тимлид дает вам срочное задание: скачать 1000 изображений для завтрашней презентации и подсчитать их общий размер. Предыдущий исполнитель не справился, и теперь все на ваших плечах. Время ограничено, и только асинхронный код может помочь. Удачи!

# целевая страница: https://asyncio.ru/zadachi/4/index.html

# Цель:
# Скачать 1000 изображений с целевой веб-страницы.
# Подсчитать общий размер всех скачанных изображений.

# ссылка на задачу - https://stepik.org/lesson/1075354/step/5?unit=1085452

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_img_size(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                return int(response.headers['Content-Length'])

async def main():
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
            async with session.get(r'https://asyncio.ru/zadachi/4/index.html') as response:
                page = await response.text()
                soup = BeautifulSoup(page, 'html.parser')
                main_tag = soup.find('main')
                img_tags = main_tag.find_all('img')
                tasks = [get_img_size(r'https://asyncio.ru/zadachi/4/' + tag['src'], semaphore) for tag in img_tags]
                results = await asyncio.gather(*tasks)
                print(sum(results))

asyncio.run(main())