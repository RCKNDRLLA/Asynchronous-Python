# �� - ������� �� ������������ � �������� �������� ��������-����������. 
# ����� ��������� ��������� � ������������� ����������� ������ �������� ���������� ����� ���� ������. �� �������� ������ ������� �����, ����� ����������, ���� �� ������ �������� ������� ������� � �������� ��������. ���� ������� ������������ ��� ����, �� � �������, ������� �� ����� ������ ��� �������(JSON). 
# ������ ���� ������ - ������������� ���� ������ �� ���-�� ����� ������� ��� �������(CSV) , ����� �������� ����� ����� ������ ������� ����� ����������.
# ���� ������ - �������� ����������� ��� ��� ��������� � ������� ���-������ �� 10 ���, � ������ �������� ������� ������������� � ��������� CSV ����.
# https://stepik.org/lesson/1029069/step/8?unit=1037339

import asyncio
import aiocsv
import json
import aiofiles
import aiofiles.os as o
from datetime import datetime

async def log_load(file_name):
    res = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            if item['HTTP-статус'] == 200:
                res.append(item)
    return res

async def main():
    res = []
    dirs = await o.listdir(r'C:\Users\Lenovo\Dev\asyncio\logs')
    tasks = [log_load(r'C:\Users\Lenovo\Dev\asyncio\logs\\' + file_name) for file_name in dirs]
    results = await asyncio.gather(*tasks)
    for result in results:            
        res.extend(result)
    res.sort(key=lambda x: x['Время и дата'])
    for item in res:
            datetime_str = item['Время и дата']
            dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            formatted_date_time = dt.strftime('%d.%m.%Y %H:%M:%S')
            item['Время и дата'] = formatted_date_time
    
    
    async with aiofiles.open(r'C:\Users\Lenovo\Dev\asyncio\answer_logs.csv', mode='w', encoding='utf-8-sig', newline='') as output:
        writer = aiocsv.AsyncDictWriter(output, delimiter=';', lineterminator='\n', fieldnames=['Время и дата', 'IP-адрес', 'User-Agent', 'Запрошенный URL', 'HTTP-статус', 'Реферер', 'Cookie', 'Размер страницы и заголовки ответа', 'Метод запроса', 'Информация об ошибке'])
        await writer.writeheader()
        await writer.writerows(res)
asyncio.run(main())