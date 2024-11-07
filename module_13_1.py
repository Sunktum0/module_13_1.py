import time
import asyncio

async def  start_strongman(name, power):
    print(f'Силач {name} начал соревнование')

    for ball_number in range(1, 6):
        # Задержка обратно пропорциональная силе
        delay = 1 / power  # Чем больше сила, тем меньше задержка
        await asyncio.sleep(delay)  # Ждем соотношение времени

        # Выводим сообщение о поднятии шара
        print(f'Силач {name} поднял {ball_number} шар.')

        # Выводим сообщение о завершении соревнований
    print(f'Силач {name} закончил соревнования.')

async def  start_tournament():
    task_1 = asyncio.create_task(start_strongman("Pasha", 3))
    task_2 = asyncio.create_task(start_strongman("Denis", 4))
    task_3 = asyncio.create_task(start_strongman("Apollon", 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
