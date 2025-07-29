# Задача: Напишите асинхронный код, который имитирует обработку логов событий сервера. Каждое событие имеет свою уникальную задержку обработки (на ответ сервера).

# Описание компонентов задачи:
# Набор данных log_events: Это список словарей, где каждый словарь представляет событие и соответствующую задержку его обработки. Событие описывается через ключ event, а задержка — через ключ delay. Задержки установлены таким образом, чтобы каждое событие обрабатывалось асинхронно с уникальной задержкой.

# Пример данных
# log_events = [
#    {"event": "Запрос на вход", "delay": 0.5},
#    {"event": "Запрос данных пользователя", "delay": 1.0},
#    {"event": "Обновление данных пользователя", "delay": 1.5},
#    ...
#    {"event": "Обновление конфигурации сервера", "delay": 5.0}
#    ]

# ссылка на задачу - https://stepik.org/lesson/933677/step/8?unit=939576

import asyncio

async def fetch_log(event):
    await asyncio.sleep(event["delay"])
    return f"Событие: {repr(event['event'])} обработано с задержкой {event['delay']} сек."

async def main():
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    result = await asyncio.gather(*tasks)
    for i in result:
        print(i)
        
asyncio.run(main())