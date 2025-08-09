# Напишите код, который симулирует асинхронную загрузку файлов с проверкой статуса задачи каждую секунду. У вас есть коллекция из 20 файлов различных типов и размеров, которые нужно "загрузить". 

# Исходные данные:
# Словарь files, где ключ — это имя файла, а значение — размер файла в мегабайтах.
# Фиксированная скорость сети — 8 мегабайт в секунду

# Расчет времени загрузки: Программа должна вычислять время, необходимое для скачивания каждого файла, исходя из его размера и скорости сети. Время загрузки рассчитывается как размер файла / скорость сети. Используйте  asyncio.sleep() для имитации загрузки файлов по формуле выше.

# Цели Задачи:
# Разработать логику для регулярной проверки и отображения статуса загрузки каждого файла, каждые 1 сек, начиная сразу после после запуска задач загрузки файлов.

# ссылка на задачу - https://stepik.org/lesson/933726/step/4?unit=939625

import asyncio

# Словарь файлов и их размеров
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
    print(f'Начинается загрузка файла: {file}, его размер {size} мб, время загрузки составит {time} сек')
    await asyncio.sleep(time)
    print(f'Загрузка завершена: {file}')

async def monitor_tasks(tasks):
    for task in tasks:
        status = ('в процессе','завершена')[task.done()]
        print(f'Задача {task.get_name()}: {status}, Статус задачи {task.done()}')


async def main():
    tasks = [asyncio.create_task(download_file(file, size, 8)) for file, size in files.items()]
    done = set()
    for task, file in zip(tasks, files.keys()):
        task.set_name(file)
    
    while tasks:
        await monitor_tasks(done.union(set(tasks)))
        done, tasks = await asyncio.wait(tasks, timeout=1)
    await monitor_tasks(done)    
    print('Все файлы успешно загружены')


asyncio.run(main())
