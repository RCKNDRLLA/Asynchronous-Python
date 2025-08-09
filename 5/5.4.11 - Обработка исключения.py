# ¬аша задача (почти та же что и в 4 степе) Ч дописать корутину main(), котора€ создаст задачу дл€ корутины coroutine() и запланирует еЄ выполнение.  орутина main() должна обработать исключение и напечатать сообщение об ошибке, сгенерированное в coroutine().

# raise ValueError('—екретный код')
#  орутина coroutine() скрыта "под капотом" с ней можно работать из  main().

# coroutine() выполн€ет только одно действие, возбуждает исключение c сообщением об ошибке (в котором хранитс€ секретный код).

# ссылка на задачу - https://stepik.org/lesson/933727/step/11?unit=939626

import asyncio

async def main():
    task = asyncio.create_task(coroutine())
    try:
        await task
        print(task.result())
    except ValueError as e:
        print(e)


asyncio.run(main())