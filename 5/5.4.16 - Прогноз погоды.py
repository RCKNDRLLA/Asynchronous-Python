# � ��� ���� ��������� ���������� ������ (API) ��� ��������� ������, � ��� ����� �������� ��������� �� �������, ������� �������.

# ������������ ��� ������� ������: 

# �������� �������� fetch_weather():
# �������� ������ ������� ����� � ������� ���������� ������� �� 1 �� 5 ������ ������������.
# ����� �������� �������� ������ "��������" ������ � �����������: ����� ��������� �������� � ��������� �� -10 �� +35 �������� ������������.
# ����������� ��������� �������� �������� � ����������� ������� random.randint() � �� ������� �������� random.seed().
# �������� ������ ���������� ��������� � �������: 
# f"������ � ������ �������� �� ��������� {source} ��� ������ {city}: {temperature}�C"
# � �������� main() ��������� ������ ��� ������� ��������� ������, ���������� � ������ sources, ��� ������ ���������� � ���������� city. ��������� ��������� ������ �� ������� ��������� � �������� ��������� �� �����. ���������� ���������� ��������� ����� �� �����.

# ������ �� ������ - https://stepik.org/lesson/933727/step/16?unit=939626

import asyncio
import random

# �� ������!
random.seed(0)

async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(1, 5))
    t = random.randint(-10, 35)
    return f"������ � ������ �������� �� ��������� {source} ��� ������ {city}: {t}�C"

async def main():
    city = "������"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]
    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    result = tuple(done)[0].result()
    print(result)
    

asyncio.run(main())