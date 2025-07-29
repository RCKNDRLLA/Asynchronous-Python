# Вам предоставлен список из 100 новостных заголовков.

# news_list = [
#    "Новая волна COVID-19 обрушилась на Европу",
#    "Рынки акций растут на фоне новостей о вакцине",   
#     ....
# Остальные вшиты в задачу

# Ваша задача — создать асинхронную программу с тремя задачами, которые анализируют этот список на предмет наличия определенных ключевых слов:

# "COVID-19", "игр", "новый вид"

# При обнаружении совпадения ключевого слова в новостном заголовке корутина должна выполнить какую-то задержку, чтобы имитировать длительную операцию  обработки данных (формирование отчета) и вывести сообщение о найденном соответствии, указывая ключевое слово и соответствующий заголовок новости.
 
# ссылка на задачу - https://stepik.org/lesson/933679/step/12?unit=939578

import asyncio

async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword in news:
            await asyncio.sleep(delay)
            print(f"Найдено соответствие для '{keyword}': {news}")


async def main():
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 1))
    task2 = asyncio.create_task(analyze_news('игр', news_list, 1))
    task3 = asyncio.create_task(analyze_news('новый вид', news_list, 1))
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
