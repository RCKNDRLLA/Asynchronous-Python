# ���� ������ (����� �� �� ��� � � 4 �����) � �������� �������� main(), ������� ������� ������ ��� �������� coroutine() � ����������� � ����������. �������� main() ������ ���������� ���������� � ���������� ��������� �� ������, ��������������� � coroutine().

# raise ValueError('��������� ���')
# �������� coroutine() ������ "��� �������" � ��� ����� �������� ��  main().

# coroutine() ��������� ������ ���� ��������, ���������� ���������� c ���������� �� ������ (� ������� �������� ��������� ���).

# ������ �� ������ - https://stepik.org/lesson/933727/step/11?unit=939626

import asyncio

async def main():
    task = asyncio.create_task(coroutine())
    try:
        await task
        print(task.result())
    except ValueError as e:
        print(e)


asyncio.run(main())