import asyncio


async def say_hello_async():
    await asyncio.sleep(2)
    print("Hello, Async world!")


async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)
    print("Finished another task!")


async def main():
    await asyncio.gather(
            say_hello_async(),
            do_something_else(),
            )


if __name__ == "__main__":
    asyncio.run(main())
