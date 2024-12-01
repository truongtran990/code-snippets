import requests
import time


def fetch(url):
    return requests.get(url).text


def main():
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        fetch(url)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Done in {time.time() - start_time} seconds")
