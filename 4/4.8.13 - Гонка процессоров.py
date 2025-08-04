# Используйте предоставленный словарь processor_delays, где ключи — это названия процессоров, а значения ключей — это имитированное время (в секундах), необходимое для тестирования каждого процессора.

# Допишите функцию simulate_processing, которая принимает время задержки. Функция должна имитировать процесс тестирования процессора, используя await asyncio.sleep(delay), где delay это время задержки из словаря.

# Организуйте асинхронные задачи для каждого процессора, передавая в них соответствующие названия с помощью аргумента  name=name для функции asyncio.create_task() и задержки из словаря processor_delays.

# С помощью await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED) определите первую завершенную задачу, что указывает на самый быстрый процессор. Выведите название этого процессора как победителя соревнования.
# print(f"Первый завершенный процесс: {task.get_name()}")
# Код должен вывести только одну строку с самым быстрым процессором.

# ссылка на задачу - https://stepik.org/lesson/933688/step/13?unit=939587

import asyncio

processor_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
}


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(delay), name=name) for name, delay in processor_delays.items()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"Первый завершенный процесс: {task.get_name()}")


asyncio.run(main())