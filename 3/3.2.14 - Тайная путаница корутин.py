# ���� ������: ��������� ������� �������. ��� �����:

# ��������������� ��� ���� � ���������� ��������, ������� �������� ������ ����� � ���������
# ��������� ��� �������� � ����� asyncio.run()

# ������ �� ������ - https://stepik.org/lesson/933699/step/14?unit=939598

import asyncio


async def coro_1():
    print("������� �������� 0")


async def coro_5():
    print("������� �������� 3")
    await coro_3()


async def coro_3():
    print("������� �������� 2")
    await coro_2()


async def coro_4():
    print("������� �������� 1")
    await coro_1()


async def coro_2():
    print("������� �������� 4")
    await coro_4()


asyncio.run(coro_5())