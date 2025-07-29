# ���� ������ - �������� ����������� ��� �� Python, ������� ����� ��������� ��������� ���������, ������������, ����������, �������� ������������, �������������� � �������� �������. ������ �� ���� �������� ������� ������ ���������� �������, ������� ���������� � ��������. ��� ��� ������ ��������� ��������� ��� ��� �������� � ���������� ������ ������ �������� � �������� �������.

# ������ �� ������ - https://stepik.org/lesson/933689/step/11?unit=939588

import asyncio

action_messages = {
    'activate': '��������� ������� � ��������, ��������� �������: {} ������',
    'perform': '������������ � ��������, ��������� �������: {} ������',
    'recharge': '���������� �������, ��������� �������: {} ������',
    'check': '�������� ������������ �������, ��������� �������: {} ������',
    'restore': '�������������� �������, ��������� �������: {} ������',
    'close': '�������� �������, ��������� �������: {} ������',
}

result_messages = {
    'activate': '��������� ��������� �������: {} ������ �������',
    'perform': '��������� ������������: {} ������ �������',
    'recharge': '��������� ���������� �������: {} ������ �������',
    'check': '��������� �������� ������������: {} ������ �������',
    'restore': '��������� �������������� �������: {} ������ �������',
    'close': '��������� �������� �������: {} ������ �������',
}

calcs = {
    'activate': lambda x: x * 2,
    'perform': lambda x: x + 2,
    'recharge': lambda x: x * 3,
    'check': lambda x: x + 4,
    'restore': lambda x: x * 5,
    'close': lambda x: x - 1,
}

ORDER_ACTIONS = {
    'start': ['activate'],
    'process': ['perform', 'recharge', 'check', 'restore'],
    'finish': ['close'],
}


async def action(future, name_action, time_action):
    print(action_messages.get(name_action).format(time_action))
    await asyncio.sleep(time_action)
    future.set_result(calcs.get(name_action)(time_action))


async def portal_operator():
    time_arg = 2
    result = []

    loop = asyncio.get_event_loop()

    for phase in ('start', 'process', 'finish'):
        futures = []
        tasks = []

        for name_action in ORDER_ACTIONS[phase]:
            future = loop.create_future()
            futures.append((name_action, future))
            task = asyncio.ensure_future(action(future, name_action, time_arg))
            tasks.append(task)
        await asyncio.gather(*tasks)
        for name_action, future in futures:
            result.append(result_messages.get(name_action).format(time_arg))

        # ������� time_arg
        last_future_in_phase = futures[-1][1]
        time_arg = last_future_in_phase.result()

    print('\n'.join(result))


asyncio.run(portal_operator())