import asyncio
import aiofiles
import aiocsv
from aiofiles import os
import os as o
import json


async def logger(file_name, semaphore):
    res = {}
    async with semaphore:
        async with aiofiles.open(file_name, mode='r', encoding='cp1241', newline='') as file:
            reader = aiocsv.AsyncDictReader(file, fieldnames=['Марка авто',
                                                              'Год выпуска авто',
                                                              'Место положения авто',
                                                              'Стоимость авто',
                                                              'Состояние авто'])
            async for row in reader:
                status = row['Состояние авто']
                res[status] = res.get(status, 0) + row['стоимость авто']
                    
    return res

async def main():
    semaphore = asyncio.Semaphore(1000)
    tasks = []
    walker = o.walk(r"C:\Users\Lenovo\Dev\asyncio\auto")
    for path, dirs, files in walker:
        for file in files:
            tasks.append(asyncio.create_task(logger(path + '\\' + file, semaphore)))

    results = await asyncio.gather(*tasks)
    res = []
    for result in results:
        if result:
            res.extend(result)  

    async with aiofiles.open(r"C:\Users\Lenovo\Dev\asyncio\answer.json", mode='w', encoding='utf-8') as output:
        await output.write(json.dumps(res, ensure_ascii=False, indent=4))

asyncio.run(main())