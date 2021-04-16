import json
import aiofiles
import requests
import asyncio
import aiohttp


async def aio_download(cid, _b_id, title):
    data = {
        "book_id": _b_id,
        "cid": f"{_b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    data_url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(data_url) as resp:
            dic = await resp.json()

            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def get_catalog(_url):
    resp = requests.get(_url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(aio_download(cid, b_id, title))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(get_catalog(url))
