from threading import Thread, current_thread
from multiprocessing import Pipe
from multiprocessing.connection import Connection


class Writer(Thread):
    def __init__(self, conn: Connection) -> None:
        super().__init__()
        self.conn = conn
        self.name = "Writer"

    def run(self) -> None:
        print(f"{current_thread().name}: Sending rubber duck...")
        self.conn.send("Rubber duck")


class Reader(Thread):
    def __init__(self, conn: Connection) -> None:
        super().__init__()
        self.conn = conn
        self.name = "Writer"

    def run(self) -> None:
        print(f"{current_thread().name}: Reading...")
        msg = self.conn.recv()
        print(f"{current_thread().name}: Received: {msg}")


def main() -> None:
    reader_conn, writter_conn = Pipe()
    reader = Reader(reader_conn)
    writer = Writer(writter_conn)

    threads = [
            writer,
            reader,
            ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
