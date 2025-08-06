# Предлагаем вам создать и запустить корутину main() не через высокоуровневый asyncio.run(), а с помощью метода loop.run_until_complete().

# Корутина main() должна выводить на экран сообщение: "Корутина завершена".
# Корутина должна быть запущена с помощью метода loop.run_until_complete().
# При создании цикла событий вручную, сохраните его в переменную loop.
# Не забудьте закрыть цикл событий после завершения работы корутины. 

# ссылка на задачу - https://stepik.org/lesson/933692/step/7?unit=939591

import asyncio

async def main():
    print("Корутина завершена")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()