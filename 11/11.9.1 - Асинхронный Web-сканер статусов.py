#  Вы работаете в отделе кибербезопасности в крупной IT-компании. Ваша команда получила информацию о том, что на одном из образовательных сайтов по асинхронному программированию спрятан секретный код. Этот код представляет собой числовую последовательность, которая, как утверждается, является ключом к расшифровке важного сообщения.

#  Ваша задача — написать асинхронный скрипт на Python, который будет сканировать веб-страницы, собирать их статус-коды и суммировать их.

# Выходные данные:
# Необходимые страницы находятся в диапазоне: 
# https://asyncio.ru/zadachi/5/1.html
# ...
# ...
# ...
# https://asyncio.ru/zadachi/5/1000.html

# Семафор: Используйте семафор для ограничения количества одновременных запросов. Сервер слабоват, так что рекомендуется использовать ограничение для него в 10 (+/-).
# Получение статус-кода: Сделайте GET-запрос к странице и добавьте статус-код в список status_codes=[].
# Вставьте число, которые у вас получилось после суммирования всех обработанных статус-кодов. 

# ссылка на задачу - https://stepik.org/lesson/1075354/step/1?unit=1085452

import aiohttp
import asyncio
from aiohttp.client import ClientResponse


# Колбэк-функции для обработчиков
async def scan_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as response:
                return response.status


async def main():
    semaphore = asyncio.Semaphore(10)
    tasks = [scan_url(fr'https://asyncio.ru/zadachi/5/{i}.html', semaphore) for i in range(1, 1001)]
    results = await asyncio.gather(*tasks)
    print(sum(results))

asyncio.run(main())