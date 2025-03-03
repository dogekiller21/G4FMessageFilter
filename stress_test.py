
import sqlite3
import time

import asyncio

from app.predictions.client import get_client
from app.predictions.models import G4FModel
from app.predictions.prompts import execute_prompt


async def semaphore_wrapper(semaphore, coro, index):
    async with semaphore:
        try:
            print(f"fetching {index} {time.time()}")
            await coro
        except Exception as e:
            print(f"Error {index} {time.time()}: {e}")
        else:
            print(f"Success {index} {time.time()}")


async def main():
    client = get_client()
    connection = sqlite3.connect("messages.db")
    cursor = connection.cursor()
    cursor.execute("SELECT message_text FROM messages ORDER BY date DESC LIMIT 1000")
    rows = cursor.fetchall()

    semaphore = asyncio.Semaphore(100)
    tasks = []
    start_time = time.time()

    for index, row in enumerate(rows, start=1):
        message_text = row[0]
        tasks.append(
            semaphore_wrapper(
                semaphore=semaphore,
                coro=execute_prompt(
                    client=client,
                    prompt=message_text,
                    model=G4FModel.deepseek_v3
                ),
                index=index)
        )
    await asyncio.gather(*tasks)
    print(f"Done in {time.time() - start_time}")


if __name__ == "__main__":
    asyncio.run(main())