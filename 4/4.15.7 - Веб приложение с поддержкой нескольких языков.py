# � ������ ������ ��������� �������� ���� �� ��������� ����, � ������� ������������� ����������� ���������� ����� ���� ����� �������.

# �����������, ��� � ��� ���� ������� ���-����������, ����������� ���������� ����������� � �������������� ��������� �� ������ ������. ������������ ��� �������������� (��� � �������� ������ � �����������) �������� ������ ���� �� ������ ���������. ����� ����� ��� ��������� ������������ �� ��������� �����. ��� ���� �� ��������� ���������� ���������� � ���������� ����� ������� � ����������� ���. ����� �� ���������� � �������� ��������� ��� ������ ����� ������� ��������� ������������� ���� - ���������� ������� ��� ��������. ���������� ��������������� ��� ����� ������ ������������ �����������.

# �������� ������: 

# �� ������ ������ ���������� ������������ 3 �����: 
# en: ����������
# ru: �������
# es: ���������

# �� ������� ������ ���������� ����� ���������� �������������� ��������� � ��������� �� ������. ������ ��������� �� ���� ������ ��� ������� � ������� ���� � ��������������� ��������. 

# ������ �� ������ - https://stepik.org/lesson/1397809/step/7?unit=1414690

import asyncio
import contextvars

# ����������� ���������� ��� �������� �������� �����
current_language = contextvars.ContextVar('current_language')

def set_language(language_code):
    current_language.set(language_code)

async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "������!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]

async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "��������� ������.",
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