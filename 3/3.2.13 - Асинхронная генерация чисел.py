# Создайте корутину generate(), которая принимает число в качестве аргумента, имитирует время ожидания I/O-bound операции (используйте await asyncio.sleep(0.1)) и затем выводит сообщение в формате:
# "Корутина generate с аргументом {число}"
# Создайте корутину main(). Внутри этой корутины:
# Сгенерируйте последовательность чисел от 0 до 9 (включительно).
# Передайте каждое из этих чисел в корутину generate().
# Выполните все корутины.
# Используйте функцию asyncio.run(), чтобы запустить корутину main().

# ссылка на задачу - https://stepik.org/lesson/933699/step/13?unit=939598

import asyncio

async def generate(digit):
    await asyncio.sleep(0.1)
    print(f"Корутина generate с аргументом {digit}")
    
async def main():
    for i in range(10):
        await generate(i)
        
asyncio.run(main())