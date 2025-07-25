# В древнем королевстве ремесленники используют дерево из леса для создания предметов для героев королевства. Ваша задача состоит в том, чтобы симулировать рабочий процесс ремесленников с использованием асинхронного программирования.

# Цель: Создать асинхронный код, который реализует взаимодействие между двумя корутинами: одной, которая добывает древесину, и другой, которая изготавливает предметы из этой древесины.

# Ссылка на задачу - https://stepik.org/lesson/933712/step/10?unit=939611

import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}


async def gather_wood(condition, event):
    while not event.is_set():
        async with condition:    
            await asyncio.sleep(0.1)
            main.storage += 2
            print(f"Добыто 2 ед. дерева. На складе {main.storage} ед.")
            condition.notify()
        await asyncio.sleep(0)


async def craft_item(condition, event):
    for item, wood_required in wood_resources_dict.items():
        async with condition:
            while main.storage < wood_required:
                await condition.wait()
            main.storage -= wood_required
            print(f"Изготовлен {item}.")
    event.set()
        
            
async def main():
    main.storage = 0
    event = asyncio.Event()
    condition = asyncio.Condition()
    task2 = asyncio.create_task(craft_item(condition, event))
    task1 = asyncio.create_task(gather_wood(condition, event))
    await asyncio.gather(task2, task1)


asyncio.run(main())