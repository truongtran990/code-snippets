import aiohttp
import asyncio
from codetiming import Timer


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Starting...")
            print(f"Status: {response.status}")
            print(f"Content-type: {response.headers['content-type']}")
            data = await response.text()
            print("Completed...\n")
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
    with Timer(text="Total elapsed time: {:.1f}"):
        for url in urls:
            await fetch(url)
        print("all good")


if __name__ == "__main__":
    asyncio.run(main())
