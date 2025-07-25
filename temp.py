import asyncio

async def worker(name, shared_var, lock, event):
    while True:
        # ждём, пока есть изменение
        await event.wait()
        async with lock:
            print(f"{name} sees change: {shared_var['value']}")
            # после прочтения сбрасываем событие
            event.clear()

        await asyncio.sleep(1)  # симуляция работы

async def main():
    shared_var = {'value': 0}  # общий словарь
    lock = asyncio.Lock()
    event = asyncio.Event()

    # запускаем две корутины-работника
    task1 = asyncio.create_task(worker("Worker 1", shared_var, lock, event))
    task2 = asyncio.create_task(worker("Worker 2", shared_var, lock, event))

    # корутина, которая меняет переменную
    for i in range(5):
        await asyncio.sleep(2)
        async with lock:
            shared_var['value'] += 1
            print(f"Main: incremented value to {shared_var['value']}")
            event.set()  # уведомляем всех, что есть изменение

    await asyncio.sleep(2)
    task1.cancel()
    task2.cancel()

asyncio.run(main())