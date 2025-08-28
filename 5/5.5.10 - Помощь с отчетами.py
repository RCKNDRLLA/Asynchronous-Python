# Вы работаете над модернизацией системы для крупного финансового учреждения, где аналитики часто загружают большие объемы данных для последующего анализа. Ваша задача состоит в том, чтобы создать тестовую систему для асинхронного скачивания данных с возможностью отмены. Если во время скачивания аналитик понимает, что эти данные больше не нужны (например, он обнаружил ошибку в параметрах запроса), задача может быть отменена. 

# Для тестирования вам нужно запустить загрузку нескольких отчетов для разных пользователей. Список отчетов и время их загрузки представлены в списке reports:

# Для пользователя "Дмитрий Орлов" задачу нужно отменить. Инициировать отмену задачи нужно из самой задачи. Для остальных пользователей отчет должен быть загружен.

# ссылка на задачу - https://stepik.org/lesson/933728/step/10?unit=939627

import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]

async def download_data(report):
    name = report['name']
    report_name = report['report']
    if name == 'Дмитрий Орлов':
        await cancel_task(asyncio.current_task())
        print(f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные")
    else:
        await asyncio.sleep(report['load_time'])
        print(f"Отчет: {report_name} для пользователя {name} готов")

async def cancel_task(task):
    task.cancel()

async def main():
    tasks = [asyncio.create_task(download_data(report)) for report in reports]
    try:
        await asyncio.gather(*tasks, return_exceptions=True)
    except asyncio.CancelledError as e:
        pass


asyncio.run(main())