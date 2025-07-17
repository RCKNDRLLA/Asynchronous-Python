import asyncio
import aiofiles
import aiocsv
import json

async def main():
    res = []
    async with aiofiles.open(r"C:\Users\Lenovo\D9ev\asyncio\region_student\Задача Студенты", encoding='utf-8-sig') as file:
        reader = aiocsv.AsyncDictReader(file, delimiter=';')
        async for row in reader:
            res.append(row)

    with open(r'C:\Users\Lenovo\Dev\asyncio\auto', mode='w', encoding='utf-8') as output:
        await output.write(json.dump(res, ensure_ascii=False, indent=4))
        

asyncio.run(main())