# �������� ������ � �������� ������:
# �������� ����������� ��� ��� ���������� ��������� ����� � �������� � ������ ������������� ������� �� �� ����������. 

# ������ ������ ������� �� ���������� ������ (��������). ������ �������� ��������� �������� ������� ���������� ������ ������, ����� ���������� �� ������������� ����������. �� ������� �� ���������� ������ ������ ����� ���� �������� �������� 5 ������.

# ���� � ���������� tasks_dependencies ������� ��� ������ � ���������, � ����� ����� ���������� ������ ���������.

# tasks_dependencies = {}
 
# ����� �������:
# ���������� ����������� ���������� ������ ������ ������, ��������� ������� asyncio.gather(). ����� ������ ������ ����������� ������� ��� ������ ������, ���������� � �������� ������. 
�.�. ��� ������ "����������_���������" ������������ ����� ����� � ���� ������� ������ ���� ���������:

# ?{"��������": "��������� ������������ ���������", "�����": 1},
# {"��������": "��������� ������� ������������", "�����": 2},
# {"��������": "��������� ������� �������� ������", "�����": 3},
# {"��������": "�������� ������� ��������", "�����": 4},
# {"��������": "������������ �������� �����", "�����": 4},
# {"��������": "�������� ��������� ���������", "�����": 6},
# {"��������": "�������� ��������� ������������", "�����": 8}
?
# ����� ����� �� ���������� ���� ������ ������ ������ ������ ���� �� ����� 5 ������.

# ��� ���� ���� ������ ����� ����������� ��� ���������������, ��� � ������������. 

# ������ �� ������ - https://stepik.org/lesson/933681/step/10?unit=939580

import asyncio

# ������� tasks_dependencies = {} ���� � ������, ��������� ��� � ������� �� �����.
async def execute_subtask(task_name, duration):
    if duration <= 5:
        await asyncio.sleep(duration)
        print(f'���������: {task_name} ������ ����������� � ����, �� {duration} ���.')
        return True
    else:
        print(f'���������: {task_name} �� ������ ����������� � ����, �� {duration} ���.')
        return False
    
async def execute_task(task_name, subtasks):
    result = await asyncio.gather(*(execute_subtask(subtask['��������'], subtask['�����']) for subtask in subtasks))
    if all(result):
        print(f'������: {task_name} = ��� ��������� ���������.')
    else:
        print(f'������: {task_name} �� ����������� � ����, �.�. ���� ��� ��������� �������� ������ ������� ����� �������.')


async def main():
    for i in tasks_dependencies:
        await execute_task(i, tasks_dependencies[i]['�����'])


asyncio.run(main())