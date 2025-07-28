# Создайте две корутины: coro_1() и coro_2().
# Каждая из корутин при вызове должна выводить своё уникальное приветственное сообщение.
# Корутины должны "поприветствовать" друг друга в своих сообщениях.
# Создайте корутину main(), в которой запустите обе корутины, сначала корутину coro_1(),затем coro_2().
# Используйте функцию asyncio.run(), чтобы запустить корутину main().

# ссылка на задачу - https://stepik.org/lesson/933699/step/12?unit=939598

import asyncio

async def coro_1():
    print('coro_1 says, hello coro_2!')    
    
async def coro_2():
    print('coro_2 says, hello coro_1!')
    
async def main():
    await coro_1()
    await coro_2()
    
asyncio.run(main())