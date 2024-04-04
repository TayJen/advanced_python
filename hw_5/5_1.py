import os
import time

import aiohttp
import aiofiles
import asyncio


RANDOM_PHOTO_LINK = "https://picsum.photos/1920/1080"
FOLDER_TO_SAVE = "./artifacts/5_1_images"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(RANDOM_PHOTO_LINK) as response:
            if response.status == 200:
                f = await aiofiles.open(os.path.join(FOLDER_TO_SAVE, f'{time.time()}.jpg'), mode='wb')
                await f.write(await response.read())
                await f.close()


if __name__ == '__main__':
    num_files = int(input())
    os.makedirs(FOLDER_TO_SAVE, exist_ok=True)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(main()) for _ in range(num_files)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
