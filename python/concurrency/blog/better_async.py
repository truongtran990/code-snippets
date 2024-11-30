import asyncio
import aiohttp
from codetiming import Timer


async def get(session: aiohttp.ClientSession, url):
    print(f"Start requesting URL: {url}")
    response = await session.get(url)
    data = await response.json()
    return data


async def main():
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]

    with Timer(text="\nTotal elapsed time: {:.1f}"):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in urls:
                tasks.append(asyncio.create_task(get(session, url)))
            await asyncio.gather(*tasks, return_exceptions=True)
    return True


if __name__ == "__main__":
    asyncio.run(main())
