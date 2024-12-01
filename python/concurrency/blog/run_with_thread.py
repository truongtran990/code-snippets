import threading
from codetiming import Timer
import requests
import concurrent.futures


def fetch(session: requests.Session, url):
    print(f"Start requesting URL: {url}")
    response = session.get(url)
    print(f"Receive: {response}")
    return response


def main():
    urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    with Timer(text="\nTotal elapsed time: {:.1f}"):
        with requests.Session() as session:
            for url in urls:
                pool.submit(fetch, session, url)


if __name__ == "__main__":
    main()
