# ��� ������������ ������ �� 100 ��������� ����������.

# news_list = [
#    "����� ����� COVID-19 ���������� �� ������",
#    "����� ����� ������ �� ���� �������� � �������",   
#     ....
# ��������� ����� � ������

# ���� ������ � ������� ����������� ��������� � ����� ��������, ������� ����������� ���� ������ �� ������� ������� ������������ �������� ����:

# "COVID-19", "���", "����� ���"

# ��� ����������� ���������� ��������� ����� � ��������� ��������� �������� ������ ��������� �����-�� ��������, ����� ����������� ���������� ��������  ��������� ������ (������������ ������) � ������� ��������� � ��������� ������������, �������� �������� ����� � ��������������� ��������� �������.
 
# ������ �� ������ - https://stepik.org/lesson/933679/step/12?unit=939578

import asyncio

async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword in news:
            await asyncio.sleep(delay)
            print(f"������� ������������ ��� '{keyword}': {news}")


async def main():
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 1))
    task2 = asyncio.create_task(analyze_news('���', news_list, 1))
    task3 = asyncio.create_task(analyze_news('����� ���', news_list, 1))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
