# ���������� ��� ������� � ��������� �������� main() �� ����� ��������������� asyncio.run(), � � ������� ������ loop.run_until_complete().

# �������� main() ������ �������� �� ����� ���������: "�������� ���������".
# �������� ������ ���� �������� � ������� ������ loop.run_until_complete().
# ��� �������� ����� ������� �������, ��������� ��� � ���������� loop.
# �� �������� ������� ���� ������� ����� ���������� ������ ��������. 

# ������ �� ������ - https://stepik.org/lesson/933692/step/7?unit=939591

import asyncio

async def main():
    print("�������� ���������")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()