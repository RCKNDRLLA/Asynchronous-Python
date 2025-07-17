import asyncio
import aiofiles
import aiocsv
from aiofiles import os
import os as o
import json


async def logger(file_name, semaphore):
    res = {}
    async with semaphore:
        async with aiofiles.open(file_name, mode='r', encoding='windows-1251', newline='') as file:
            reader = aiocsv.AsyncDictReader(file,  delimiter=';')
            async for row in reader:
                status = row['Состояние авто']
                price = row['Стоимость авто']
                res[status] = res.get(status, 0) + int(price)
                    
    return res

async def main():
    semaphore = asyncio.Semaphore(1000)
    tasks = []
    walker = o.walk(r"C:\Users\Lenovo\Dev\asyncio\auto")
    for path, dirs, files in walker:
        for file in files:
            tasks.append(asyncio.create_task(logger(path + '\\' + file, semaphore)))

    result = await asyncio.gather(*tasks)
    res = {}

    for item in result:
        for i in item:
            res[i] = res.get(i, 0) + item[i]
    
    async with aiofiles.open(r"C:\Users\Lenovo\Dev\asyncio\answer.json", mode='w', encoding='utf-8') as output:
        await output.write(json.dumps(res, ensure_ascii=False, indent=4))

asyncio.run(main())