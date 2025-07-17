import os

for i in range(5,6):
    os.mkdir(fr"C:\Users\Lenovo\Dev\asyncio\{i}")
    for j in range(15):
        os.mkdir(fr"C:\Users\Lenovo\Dev\asyncio\{i}\{i}.{j}")