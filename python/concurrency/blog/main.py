import queue


def task(name, work_queue: queue.Queue):
    if work_queue.empty():
        print(f"Task {name} has nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} is running")

            for _ in range(count):
                total += 1
            print(f"Task {name} total: {total}")


def main():
    work_queue = queue.Queue()

    for work in [15, 5, 10, 2]:
        work_queue.put(work)

    tasks = [("One", work_queue), ("Two", work_queue)]

    for name, _queue in tasks:
        task(name, _queue)


if __name__ == "__main__":
    main()
