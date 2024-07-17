import asyncio
import random
import os
import sys

# Эта короткая программа наглядно демонстрирует работу
# асинхронности и асинхронного программирования.
# Асинронное программирование особенно эффективно тогда,
# когда в программе есть функции, блокирующие ее:
# ожидание ответа от чего-либо: от пользователя (input)
# от стороннего сервиса (запросы aiohttp)
# bottleneck в данном случае - имитация блокирующей функции

class Process: 
    def __init__(self, file_name): 
        self.file_name = file_name
        self.sym = "+"
        self.state = str()

    def update_state(self, sym):
        self.state += sym

# Создаем объекты класса Proccess
PROCESSES = [Process("klim"), Process("yaroslav"), Process("alina"), Process("ivan"), Process("sergey")]

def print_procs():
    os.system('cls') # Очищает консоль
    for proc in PROCESSES:
        print(f"Файл {proc.file_name}({proc.sym}): {proc.state}", flush=True)
    sys.stdout.flush()

async def do_task(proc): # Делаем какую-либо работу с блокирующими вызовами
    bottleneck_index = random.randint(0, 9)
    for i in range(10):
        print_procs()
        if i == bottleneck_index:
            proc.update_state("|")
            await asyncio.sleep(3)
        else:
            proc.update_state("+")
            await asyncio.sleep(1)

async def main():
    tasks = []
    for proc in PROCESSES: # Создаем задачи
        tasks.append(asyncio.create_task(do_task(proc)))
    for task in tasks: # Выполняем их в асинхронном режиме
        await task

asyncio.run(main())