# pip install aiohttp

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/d7de3f9faf1e0ecdea27b73139fc8d3a.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/26b7e178e987be6d914bf8d1af120890.jpg"
]


async def aio_download(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(aio_download(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
