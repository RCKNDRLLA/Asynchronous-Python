# �� ��������� ��� ������������� ������� ��� �������� ����������� ����������, ��� ��������� ����� ��������� ������� ������ ������ ��� ������������ �������. ���� ������ ������� � ���, ����� ������� �������� ������� ��� ������������ ���������� ������ � ������������ ������. ���� �� ����� ���������� �������� ��������, ��� ��� ������ ������ �� ����� (��������, �� ��������� ������ � ���������� �������), ������ ����� ���� ��������. 

# ��� ������������ ��� ����� ��������� �������� ���������� ������� ��� ������ �������������. ������ ������� � ����� �� �������� ������������ � ������ reports:

# ��� ������������ "������� �����" ������ ����� ��������. ������������ ������ ������ ����� �� ����� ������. ��� ��������� ������������� ����� ������ ���� ��������.

# ������ �� ������ - https://stepik.org/lesson/933728/step/10?unit=939627

import asyncio

reports = [
    {"name": "������� ������", "report": "����� � �������� � �������", "load_time": 5},
    {"name": "����� �������", "report": "��������������� �������� �������� �������", "load_time": 4},
    {"name": "���� �������", "report": "������ �������������� ������", "load_time": 3},
    {"name": "����� ���������", "report": "����� ������������ ��������", "load_time": 2},
    {"name": "������� �����", "report": "������ ���������� �������", "load_time": 10}
]

async def download_data(report):
    name = report['name']
    report_name = report['report']
    if name == '������� �����':
        await cancel_task(asyncio.current_task())
        print(f"�������� ������ {report_name} ��� ������������ {name} �����������. ������� ����� ������")
    else:
        await asyncio.sleep(report['load_time'])
        print(f"�����: {report_name} ��� ������������ {name} �����")

async def cancel_task(task):
    task.cancel()

async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.CancelledError as e:
        pass


asyncio.run(main())