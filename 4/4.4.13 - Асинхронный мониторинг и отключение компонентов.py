# ��� ������������ ������ �� 10 ��������, ������� �������� � ���� ��������� �� "�������" �� "���������������". ���� ������ ����� �������������� ��� �������� �������� ��������� ������� ���������� �������.

#   status_list = [
#        "�������", "������", "�����������������", "������",
#        "����������", "���� ��������", "�����", "����� �����",
#        "��������", "���������������"
#    ]

# �������� ��� �������� (monitor_cpu(), monitor_memory(), monitor_disk_space()), ������ �� ������� �������� �� ���������� ������������� ���������� �������. ������ �������� ������ ��������� ����� ������ ��������, �������� ������� �������� ��������� ����������. ����� ����������� �� �������� ���������� � ������� await asyncio.sleep(0.1)

# ��� �������� ����������� ����� � ������� asyncio.create_task() ������� ���������� ��� ��� ������ ������ � ������� ��������� name.

# ����������� ��������� ����� �����: "CPU", "������", "�������� ������������"

# ������ ������ �������� ����������� asyncio.current_task().get_name() ��� ��������� ����� ������� ������. ��� ��� ����� ������������ � ������� print() ��� ������������� ������ ������� ��������, ����� ��������� ����� �������������� � ���������.

# ���� � �������� �������� �������������� ������ "���������������", �������� ������ �������� ��������� � ���������� ������������ ��������� � ������������ "���������" (�������� ��������� �������).

# ������ �� ������ - https://stepik.org/lesson/933679/step/13?unit=939578

import asyncio


async def monitor_cpu(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] ������ ��������: {status}")
        if status == '���������������':
            print(f"[{task_name}] ����������� ��������� ����������. ������������ ���������...")
            
async def monitor_memory(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] ������ ��������: {status}")
        if status == '���������������':
            print(f"[{task_name}] ����������� ��������� ����������. ������������ ���������...")
        
async def monitor_disk_space(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] ������ ��������: {status}")
        if status == '���������������':
            print(f"[{task_name}] ����������� ��������� ����������. ������������ ���������...")


async def main():
    status_list = [
        "�������", "������", "�����������������", "������",
        "����������", "���� ��������", "�����", "����� �����",
        "��������", "���������������"
    ]

    d = {monitor_cpu: 'CPU', monitor_memory: '������', monitor_disk_space: '�������� ������������'}
    tasks = [asyncio.create_task(func(status_list), name=d[func]) for func in d]
    await asyncio.gather(*tasks)


asyncio.run(main())