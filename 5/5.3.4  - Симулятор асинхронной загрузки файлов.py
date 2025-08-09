# �������� ���, ������� ���������� ����������� �������� ������ � ��������� ������� ������ ������ �������. � ��� ���� ��������� �� 20 ������ ��������� ����� � ��������, ������� ����� "���������". 

# �������� ������:
# ������� files, ��� ���� � ��� ��� �����, � �������� � ������ ����� � ����������.
# ������������� �������� ���� � 8 �������� � �������

# ������ ������� ��������: ��������� ������ ��������� �����, ����������� ��� ���������� ������� �����, ������ �� ��� ������� � �������� ����. ����� �������� �������������� ��� ������ ����� / �������� ����. �����������  asyncio.sleep() ��� �������� �������� ������ �� ������� ����.

# ���� ������:
# ����������� ������ ��� ���������� �������� � ����������� ������� �������� ������� �����, ������ 1 ���, ������� ����� ����� ����� ������� ����� �������� ������.

# ������ �� ������ - https://stepik.org/lesson/933726/step/4?unit=939625

import asyncio

# ������� ������ � �� ��������
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

async def download_file(file, size, speed):
    time = round(size/speed, 3)
    print(f'���������� �������� �����: {file}, ��� ������ {size} ��, ����� �������� �������� {time} ���')
    await asyncio.sleep(time)
    print(f'�������� ���������: {file}')

async def monitor_tasks(tasks):
    for task in tasks:
        status = ('� ��������','���������')[task.done()]
        print(f'������ {task.get_name()}: {status}, ������ ������ {task.done()}')


async def main():
    tasks = [asyncio.create_task(download_file(file, size, 8)) for file, size in files.items()]
    done = set()
    for task, file in zip(tasks, files.keys()):
        task.set_name(file)
    
    while tasks:
        await monitor_tasks(done.union(set(tasks)))
        done, tasks = await asyncio.wait(tasks, timeout=1)
    await monitor_tasks(done)    
    print('��� ����� ������� ���������')


asyncio.run(main())
