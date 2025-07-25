# В далёкой стране есть три производственных цеха: цех камня, металла и ткани. Каждый цех добывает свои ресурсы и производит из них уникальные изделия

# Цель: Написать асинхронный код, который организует добычу ресурсов (камень, металл, ткань) и последующее производство изделий из них в трех различных цехах.

# ссылка на задачу - https://stepik.org/lesson/933712/step/11?unit=939611

import asyncio

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

condition = asyncio.Condition()


async def gather_stone(event):
    while not event.is_set():
        async with condition:    
            await asyncio.sleep(0.1)
            main.stone_storage += 10
            print(f"Добыто 10 ед. камня. На складе {main.stone_storage} ед.")
            condition.notify()
        await asyncio.sleep(0)


async def gather_metal(event):
    while not event.is_set():
        async with condition:    
            await asyncio.sleep(0.1)
            main.metal_storage += 6
            print(f"Добыто 6 ед. металла. На складе {main.metal_storage} ед.")
            condition.notify()
        await asyncio.sleep(0)


async def gather_cloth(event):
    while not event.is_set():
        async with condition:    
            await asyncio.sleep(0.1)
            main.cloth_storage += 8
            print(f"Добыто 8 ед. ткани. На складе {main.cloth_storage} ед.")
            condition.notify()
        await asyncio.sleep(0)


async def craft_stone_items(event):
    for item, stone_required in stone_resources_dict.items():
        async with condition:
            while main.stone_storage < stone_required:
                await condition.wait()
            main.stone_storage -= stone_required
            print(f"Изготовлен {item} из камня.")
    event.set()
        

async def craft_metal_items(event):
    for item, metal_required in metal_resources_dict.items():
        async with condition:
            while main.metal_storage < metal_required:
                await condition.wait()
            main.metal_storage -= metal_required
            print(f"Изготовлен {item} из металла.")
    event.set()


async def craft_cloth_items(event):
    for item, cloth_required in cloth_resources_dict.items():
        async with condition:
            while main.cloth_storage < cloth_required:
                await condition.wait()
            main.cloth_storage -= cloth_required
            print(f"Изготовлен {item} из ткани.")
    event.set()


async def main():
    main.stone_storage = 0
    main.metal_storage = 0
    main.cloth_storage = 0
    stone_event = asyncio.Event()
    metal_event = asyncio.Event()
    cloth_event = asyncio.Event()
    tasks = [asyncio.create_task(func) for func in [gather_stone(stone_event), gather_metal(metal_event), gather_cloth(cloth_event), craft_stone_items(stone_event), craft_metal_items(metal_event), craft_cloth_items(cloth_event)]]
    await asyncio.gather(*tasks)
    

asyncio.run(main())