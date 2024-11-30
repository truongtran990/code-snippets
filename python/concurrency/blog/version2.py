from queue import Queue


def task(name, queue: Queue):
    while not queue.empty():
        count = queue.get()
        total = 0

        print(f"Task {name} is running")

        for _ in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main():
    work_queue = Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    is_done = False

    while not is_done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)

            if len(tasks) == 0:
                is_done = True


if __name__ == "__main__":
    main()
