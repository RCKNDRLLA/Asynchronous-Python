# В интернет-магазине каждый заказ проходит через несколько этапов: "Принят", "Обрабатывается", "Отправлен". Ваша задача — создать простую систему для отслеживания состояния заказов с использованием контекстных переменных.

# Что нужно сделать:

# Создайте контекстную переменную order_state.
# Создайте обычную синхронную функцию для изменения значения контекстной переменной set_order_state(state), в которой будет изменяться значение контекстной переменной на то, которое передано в качестве аргумента. 
# Напишите корутину process_order(), которая должна изменять состояние заказа в указанном порядке: "Принят", "Обрабатывается", "Отправлен". Для установки и изменения состояния заказа используйте функцию set_order_state(state).
# Добавьте задержку между изменением состояний, чтобы имитировать процесс обработки заказа (1 секунда перед каждым этапом).
# После каждого этапа выводите на экран сообщение: f"Заказ {order_id} сейчас в состоянии: {order_state}".
# В корутине main() одновременно запустите обработку заказов из списка orders, уже доступного в корутине main() и дождитесь их выполнения. 

# ссылка на задачу - https://stepik.org/lesson/1397809/step/6?unit=1414690

import asyncio
import contextvars

order_state = contextvars.ContextVar('order_state')

def set_order_state(state):
    order_state.set(state)


async def process_order(order_id):
    await asyncio.sleep(1)
    set_order_state('Принят')
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")
    await asyncio.sleep(1)
    set_order_state('Обрабатывается')
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")
    await asyncio.sleep(1)
    set_order_state('Отправлен')
    print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")

async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    tasks = [process_order(order) for order in orders]
    await asyncio.gather(*tasks)


asyncio.run(main())