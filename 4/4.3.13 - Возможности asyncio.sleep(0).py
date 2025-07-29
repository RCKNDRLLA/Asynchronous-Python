# Ниже в шаблоне кода уже написана асинхронная функция process_request() для обработки запросов в несколько этапов. Данная работа является CPU-bound операцией. Поэтому для имитации времени каждого этапа использована синхронная функция sleep(). В приведенном коде данная функция хоть и является корутиной - она ни в какой момент времени не может передать управление циклу событий, так как внутри нее нет ни одной ожидаемой операции. 

# Также есть готовая асинхронная функция для мониторинга прохождения этапов запроса update_status(), но она тоже не передает управление циклу событий.

# Цель:
# С помощью asyncio.sleep(0) настройте переключение контекста между двумя задачами таким образом, чтобы после завершения каждого этапа выводился текущий статус запроса.  
# Запускать функцию main() не нужно, ее запуск происходит автоматически. Ваша задача только добавить переключение контекста в нужных местах. 

# ссылка на задачу - https://stepik.org/lesson/933678/step/13?unit=939577

import asyncio
import time


async def process_request(request_name, stages, status):
    for stage_name in stages:
        await asyncio.sleep(0)
        time.sleep(0.1)  # Симулируем время выполнения этапа
        status[request_name] = stage_name
        


async def update_status(request_name, status):
    while True:
        await asyncio.sleep(0)
        print(status)
        if status == {request_name: 'Отправка уведомлений'}:
            break


async def main():
    # Исходные данные по запросу и этапам его обработки
    request_name = 'Запрос 1'
    stages = ["Загрузка данных", "Проверка данных", "Анализ данных", "Сохранение результатов", "Отправка уведомлений"]

    status = {request_name: None}

    # Создание задач для каждой корутины
    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)