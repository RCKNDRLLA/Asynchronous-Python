# �������� �������� generate(), ������� ��������� ����� � �������� ���������, ��������� ����� �������� I/O-bound �������� (����������� await asyncio.sleep(0.1)) � ����� ������� ��������� � �������:
# "�������� generate � ���������� {�����}"
# �������� �������� main(). ������ ���� ��������:
# ������������ ������������������ ����� �� 0 �� 9 (������������).
# ��������� ������ �� ���� ����� � �������� generate().
# ��������� ��� ��������.
# ����������� ������� asyncio.run(), ����� ��������� �������� main().

# ������ �� ������ - https://stepik.org/lesson/933699/step/13?unit=939598

import asyncio

async def generate(digit):
    await asyncio.sleep(0.1)
    print(f"�������� generate � ���������� {digit}")
    
async def main():
    for i in range(10):
        await generate(i)
        
asyncio.run(main())