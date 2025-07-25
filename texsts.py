import asyncio

wood_resources_dict = {
    6: 'Деревянный меч',
    12: 'Деревянный щит',
    24: 'Деревянный стул',
}

storage = 0

async def gather_wood(condition, event):
    global storage
    while not event.is_set():
        async with condition:
            await asyncio.sleep(0.1)  # Имитация работы
            storage += 2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            condition.notify_all()  # Будим craft_item
        await asyncio.sleep(0)  # Даём шанс craft_item проверить ресурсы

async def craft_item(condition, event):
    global storage
    global wood_resources_dict
    while not event.is_set():
        async with condition:
            # Ждём, пока появится достаточно ресурсов
            required = min(wood_resources_dict.keys(), default=float('inf'))
            while storage < required and wood_resources_dict:
                await condition.wait()
                if event.is_set():
                    return
                required = min(wood_resources_dict.keys(), default=float('inf'))

            # Если предметы закончились — выходим
            if not wood_resources_dict:
                event.set()
                condition.notify_all()
                return

            # Создаём предмет (самый дешёвый из доступных)
            for amount in sorted(wood_resources_dict.keys()):
                if storage >= amount:
                    print(f"Изготовлен {wood_resources_dict.pop(amount)}.")
                    storage -= amount
                    break

async def main():
    event = asyncio.Event()
    condition = asyncio.Condition()
    
    gather_task = asyncio.create_task(gather_wood(condition, event))
    craft_task = asyncio.create_task(craft_item(condition, event))
    
    await asyncio.gather(gather_task, craft_task)

asyncio.run(main())