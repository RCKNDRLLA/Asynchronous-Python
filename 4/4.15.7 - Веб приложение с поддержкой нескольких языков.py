# В данной задаче попробуем показать один из вариантов кода, в котором использование контекстных переменных может быть очень удобным.

# Представьте, что у вас есть простое веб-приложение, позволяющее отправлять уведомления и информационные сообщения на разных языках. Пользователь при аутентификации (или в процессе работы с приложением) выбирает нужный язык из списка доступных. После этого все сообщения отправляются на выбранном языке. При этом вы постоянно обновляете приложение и добавляете новые функции в программный код. Чтобы не передавать в качестве аргумента для каждой новой функции выбранный пользователем язык - желательно хранить его отдельно. Предлагаем воспользоваться для такой задачи контекстными переменными.

# Входящие данные: 

# На данный момент приложение поддерживает 3 языка: 
# en: английский
# ru: русский
# es: испанский

# На текущий момент приложение может отправлять приветственное сообщение и сообщение об ошибке. Тексты сообщения на трех языках уже указаны в шаблоне кода в соответствующих функциях. 

# ссылка на задачу - https://stepik.org/lesson/1397809/step/7?unit=1414690

import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar('current_language')

def set_language(language_code):
    current_language.set(language_code)

async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]

async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurri? un error."
    }
    return error_messages[current_language.get()]



async def test_user_actions(language_code):
    current_language.set(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main():
    tasks = [test_user_actions(language) for language in ['en', 'ru', 'es']]
    await asyncio.gather(*tasks)

asyncio.run(main())