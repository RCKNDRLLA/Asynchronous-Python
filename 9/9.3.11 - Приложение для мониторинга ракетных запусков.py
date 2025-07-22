# Вася - опытный программист, работающий над мощным асинхронным приложением для мониторинга ракетных запусков.
# Его задача - обеспечить надежное и быстрое обновление информации о запусках в реальном времени. 

# Вася создал асинхронное приложение для мониторинга ракетных запусков, и он хочет обеспечить возможность прерывания (interrupt) задачи, если в процессе мониторинга была обнаружена ошибка или число запусков стало равняться 50. Для этого он решил использовать interrupt_flag (объект .Event()), который является экземпляром asyncio.Event(). Если флаг установлен, задача должна завершить выполнение. В противном случае, она должна продолжать работу. 

# Ваша задача:
# Дописать код Васи в соответствии с поставленной задачей.

# Ваша задача: ознакомьтесь с описанием функций и напишите две функции — monitor_rocket_launches() и main().
# Подумайте, как в данном коде применить прерывания (interrupts) с помощью флага asyncio.Event() и методов .set(), .is_set(), .clear() для прерывания запущенной в функции main() Task задачи. 

# ссылка на задачу - https://stepik.org/lesson/933709/step/11?unit=939608

import asyncio
import random

error = None
count = 0
sek = 0

async def monitor_rocket_launches(event):
    global count
    global error
    global sek
    try:
        while True:
            error = random.choice((False, True, False, False))
            if error is True:
                break
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
        count += 1
        await asyncio.sleep(1)
    finally:
        print("Завершение мониторинга ракетных запусков")


async def main():
    global error
    global count
    global sek
    event = asyncio.Event()
    asyncio.create_task(monitor_rocket_launches(event))
   
    while True:
        await asyncio.sleep(5)        
        if count == 50:
            break
        elif error == True:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            break
        else:
            print(f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")
    await monitor_rocket_launches(event)
    

if __name__ == "__main__":
    asyncio.run(main())