import aiohttp
import asyncio
import time


async def async_fetch(url, session):
    async with session.get(url) as response:
        print(f"Fetching the URL: {url}")
        data = await response.text()
        print(f"Finished fetching the data for URL: {url}\n")
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in [
            "http://google.com",
            "http://yahoo.com",
            "http://linkedin.com",
            "http://apple.com",
            "http://microsoft.com",
            "http://facebook.com",
            "http://twitter.com",
        ]:
            tasks.append(asyncio.create_task(async_fetch(url, session)))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Done in {time.time() - start_time} seconds")
