# ����������� ��������������� ������� processor_delays, ��� ����� � ��� �������� �����������, � �������� ������ � ��� ������������� ����� (� ��������), ����������� ��� ������������ ������� ����������.

# �������� ������� simulate_processing, ������� ��������� ����� ��������. ������� ������ ����������� ������� ������������ ����������, ��������� await asyncio.sleep(delay), ��� delay ��� ����� �������� �� �������.

# ����������� ����������� ������ ��� ������� ����������, ��������� � ��� ��������������� �������� � ������� ���������  name=name ��� ������� asyncio.create_task() � �������� �� ������� processor_delays.

# � ������� await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED) ���������� ������ ����������� ������, ��� ��������� �� ����� ������� ���������. �������� �������� ����� ���������� ��� ���������� ������������.
# print(f"������ ����������� �������: {task.get_name()}")
# ��� ������ ������� ������ ���� ������ � ����� ������� �����������.

# ������ �� ������ - https://stepik.org/lesson/933688/step/13?unit=939587

import asyncio

processor_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
}


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(delay), name=name) for name, delay in processor_delays.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"������ ����������� �������: {task.get_name()}")


asyncio.run(main())