import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    participant_1 = asyncio.create_task(start_strongman('Кирил', 3))
    participant_2 = asyncio.create_task(start_strongman('Денис', 4))
    participant_3 = asyncio.create_task(start_strongman('Антон', 5))
    await participant_1
    await participant_2
    await participant_3


if __name__ == "__main__":
    asyncio.run(start_tournament())
