# ��� �������-����������� ������ ��� ������ �������, ������� ��� ��������� ������� �����������. ���� ������ � �������� ����������� ���, ������� ���������� ��� ��� �������� � ������ � ��� ������, ��� ����� ������� ���, ��� �������� � ������ �������. ��� ����� �� ������� ���������� �������������� ��� ��������� ��������� ����������.

# ������, � �������� �� ������ �������� ������, �� ����� ������ � ��������� ������ �� 75 �������� �� �������� � �������. �� ���� ������� ��� ���������� ������������ ������� ��� ����������� ���������� ������������� ��������, ����� �������� ���������� ��������.

# ���� problem_pages.txt �������� ������ ���������� �������, ������ �� ������� ������� �� ����� ������. ��� ������ ������������ ����� ����� �������, ������� ����� ����� ������������ ��� ������������ ������ URL-�������.

# ������� ����: https://asyncio.ru/zadachi/2/problem_pages.txt

# ������ ����������� �����:
10275454
1046410
10660263
# ��� ������� ����� �� ����� problem_pages.txt, ���������� ������������ ������ URL-�����, ������� � ���� ������� URL � ���������� .html.
# ���� ��� �������� � ����� � 10275454, �� ������ URL �����: https://asyncio.ru/zadachi/2/html/10275454.html
# ������ �������� �������� ��� <p> � id='number', � ������� ��������� �����. ��� ����� ����� ������� � �������� � ����� �����. ���� ������ � ����������� ��� ����� �� ���� ������� ����������� � �����.

# ������ �� ������ - https://stepik.org/lesson/1075354/step/3?unit=1085452

import aiohttp
import asyncio
from aiohttp.client import ClientResponse
from bs4 import BeautifulSoup
import aiofiles

async def scan_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                p_tags = soup.find('p', id='number').text
                return p_tags

async def main():
    results = []
    semaphore = asyncio.Semaphore(75)
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(fr'C:\Users\Lenovo\Dev\asyncio\11\11.9.3.txt') as file:
            page_numbers = await file.readlines()
            tasks = [scan_url(fr'https://asyncio.ru/zadachi/2/html/{number}.html', semaphore) for number in page_numbers]
            result = await asyncio.gather(*tasks, return_exceptions=True)
            results.extend(result)
    print(sum(int(result) for result in results if isinstance(result, str)))

asyncio.run(main())