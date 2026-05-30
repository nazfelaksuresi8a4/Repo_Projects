import aiohttp 
import asyncio



async def main(urls):
    async with aiohttp.ClientSession() as Session:
        tasks = [Session.get(url) for url in urls]

        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response.url)
