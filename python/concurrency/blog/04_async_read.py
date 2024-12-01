import asyncio
import aiofiles


async def async_read_file(filepath):
    async with aiofiles.open(filepath, "r") as file:
        return await file.read()


async def async_read_all(filepaths):
    tasks = [async_read_file(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)


async def main():
    filespaths = ["./data/file1.txt", "./data/file2.txt"]
    data = await async_read_all(filespaths)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
