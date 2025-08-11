# �������� ������� ���, � ������� �������� process_task() ����� ����� 1 ������� � ���������� id ������� ������. 

# � �������� main() ��������� 10 �����. �������� main() ������ ���������� ������, ���������� 10 id ����������� �����. 

# �������� �� ����� ������ �� �����.

# ������ �� ������ - https://stepik.org/lesson/933728/step/3?unit=939627

import asyncio

async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())

async def main():
    tasks = [asyncio.create_task(process_task()) for i in range(10)]
    result = await asyncio.gather(*tasks)
    return result

asyncio.run(main())