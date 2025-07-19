import aiohttp
import asyncio


# Колбэк-функции для обработчиков
async def on_request_start(session, trace_config_ctx, params):
    print("Запрос начат:", params.url)

async def on_request_end(session, trace_config_ctx, params):
    print("Запрос завершён:", params.url, params.response.status)


async def main():
    # Этот класс позволяет настроить обработчики для различных этапов HTTP-запроса
    trace_config = aiohttp.TraceConfig()

    # Добавляем обработчик для события "начало запроса".
    # Функция on_request_start() будет вызвана, когда начнется выполнение HTTP-запроса
    trace_config.on_request_start.append(on_request_start)

    # Добавляем обработчик для события "завершение запроса".
    # Функция on_request_end() будет вызвана после завершения HTTP-запроса
    trace_config.on_request_end.append(on_request_end)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.get('http://www.google.com') as response:
            print("Статус код:", response.status)


asyncio.run(main())