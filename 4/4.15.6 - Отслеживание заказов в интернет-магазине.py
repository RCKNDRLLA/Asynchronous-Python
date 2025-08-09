# � ��������-�������� ������ ����� �������� ����� ��������� ������: "������", "��������������", "���������". ���� ������ � ������� ������� ������� ��� ������������ ��������� ������� � �������������� ����������� ����������.

# ��� ����� �������:

# �������� ����������� ���������� order_state.
# �������� ������� ���������� ������� ��� ��������� �������� ����������� ���������� set_order_state(state), � ������� ����� ���������� �������� ����������� ���������� �� ��, ������� �������� � �������� ���������. 
# �������� �������� process_order(), ������� ������ �������� ��������� ������ � ��������� �������: "������", "��������������", "���������". ��� ��������� � ��������� ��������� ������ ����������� ������� set_order_state(state).
# �������� �������� ����� ���������� ���������, ����� ����������� ������� ��������� ������ (1 ������� ����� ������ ������).
# ����� ������� ����� �������� �� ����� ���������: f"����� {order_id} ������ � ���������: {order_state}".
# � �������� main() ������������ ��������� ��������� ������� �� ������ orders, ��� ���������� � �������� main() � ��������� �� ����������. 

# ������ �� ������ - https://stepik.org/lesson/1397809/step/6?unit=1414690

import asyncio
import contextvars

order_state = contextvars.ContextVar('order_state')

def set_order_state(state):
    order_state.set(state)


async def process_order(order_id):
    await asyncio.sleep(1)
    set_order_state('������')
    print(f"����� {order_id} ������ � ���������: {order_state.get()}")
    await asyncio.sleep(1)
    set_order_state('��������������')
    print(f"����� {order_id} ������ � ���������: {order_state.get()}")
    await asyncio.sleep(1)
    set_order_state('���������')
    print(f"����� {order_id} ������ � ���������: {order_state.get()}")

async def main():
    orders = ["�����1", "�����123", "�����12345"]
    tasks = [process_order(order) for order in orders]
    await asyncio.gather(*tasks)


asyncio.run(main())