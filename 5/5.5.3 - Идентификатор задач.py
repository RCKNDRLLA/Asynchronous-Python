# Ќапишите простой код, в котором корутина process_task() будет спать 1 секунду и возвращать id текущей задачи. 

# ¬ корутине main() запустите 10 задач.  орутина main() должна возвращать список, содержащий 10 id завершенных задач. 

# ¬ыводить на экран ничего не нужно.

# ссылка на задачу - https://stepik.org/lesson/933728/step/3?unit=939627

import asyncio

async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())

async def main():
    tasks = [asyncio.create_task(process_task()) for i in range(10)]
    result = await asyncio.gather(*tasks)
    return result

asyncio.run(main())