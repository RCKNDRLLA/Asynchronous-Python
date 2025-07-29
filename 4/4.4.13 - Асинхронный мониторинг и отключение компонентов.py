# Вам предоставлен список из 10 статусов, который включает в себя состояния от "Отлично" до "Катастрофически". Этот список будет использоваться для имитации проверки состояния каждого компонента системы.

#   status_list = [
#        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
#        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
#        "Критично", "Катастрофически"
#    ]

# Напишите три корутины (monitor_cpu(), monitor_memory(), monitor_disk_space()), каждая из которых отвечает за мониторинг определенного компонента системы. Каждая корутина должна проходить через список статусов, имитируя процесс проверки состояния компонента. Время затраченное на проверку имитируйте с помощью await asyncio.sleep(0.1)

# При создании асинхронных задач с помощью asyncio.create_task() укажите уникальное имя для каждой задачи с помощью аргумента name.

# Используйте следующие имена задач: "CPU", "Память", "Дисковое пространство"

# Внутри каждой корутины используйте asyncio.current_task().get_name() для получения имени текущей задачи. Это имя затем используется в функции print() для динамического вывода статуса проверки, делая сообщения более информативными и понятными.

# Если в процессе проверки обнаруживается статус "Катастрофически", корутина должна выводить сообщение о достижении критического состояния и инициировать "остановку" (имитацию остановки системы).

# ссылка на задачу - https://stepik.org/lesson/933679/step/13?unit=939578

import asyncio


async def monitor_cpu(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            
async def monitor_memory(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
        
async def monitor_disk_space(status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        task_name = asyncio.current_task().get_name()
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]

    d = {monitor_cpu: 'CPU', monitor_memory: 'Память', monitor_disk_space: 'Дисковое пространство'}
    tasks = [asyncio.create_task(func(status_list), name=d[func]) for func in d]
    await asyncio.gather(*tasks)


asyncio.run(main())