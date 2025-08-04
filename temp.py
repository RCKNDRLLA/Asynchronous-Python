def func():
    l = [1, 2, 6, 7]
    yield from l


for i in func():
    print(i)