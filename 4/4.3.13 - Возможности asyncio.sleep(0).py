# ���� � ������� ���� ��� �������� ����������� ������� process_request() ��� ��������� �������� � ��������� ������. ������ ������ �������� CPU-bound ���������. ������� ��� �������� ������� ������� ����� ������������ ���������� ������� sleep(). � ����������� ���� ������ ������� ���� � �������� ��������� - ��� �� � ����� ������ ������� �� ����� �������� ���������� ����� �������, ��� ��� ������ ��� ��� �� ����� ��������� ��������. 

# ����� ���� ������� ����������� ������� ��� ����������� ����������� ������ ������� update_status(), �� ��� ���� �� �������� ���������� ����� �������.

# ����:
# � ������� asyncio.sleep(0) ��������� ������������ ��������� ����� ����� �������� ����� �������, ����� ����� ���������� ������� ����� ��������� ������� ������ �������.  
# ��������� ������� main() �� �����, �� ������ ���������� �������������. ���� ������ ������ �������� ������������ ��������� � ������ ������. 

# ������ �� ������ - https://stepik.org/lesson/933678/step/13?unit=939577

import asyncio
import time


async def process_request(request_name, stages, status):
    for stage_name in stages:
        await asyncio.sleep(0)
        time.sleep(0.1)  # ���������� ����� ���������� �����
        status[request_name] = stage_name
        


async def update_status(request_name, status):
    while True:
        await asyncio.sleep(0)
        print(status)
        if status == {request_name: '�������� �����������'}:
            break


async def main():
    # �������� ������ �� ������� � ������ ��� ���������
    request_name = '������ 1'
    stages = ["�������� ������", "�������� ������", "������ ������", "���������� �����������", "�������� �����������"]

    status = {request_name: None}

    # �������� ����� ��� ������ ��������
    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)