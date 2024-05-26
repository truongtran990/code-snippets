import os
from multiprocessing import Process

def run_child() -> None:
    print("\n")
    print("*" * 10)
    print("Child: I am the child process")
    print(f"Child: Child's PID: {os.getpid()}")
    print(f"Child: Parent's PID: {os.getppid()}")


def start_parent(num_children: int) -> None:
    print("\n")
    print("*" * 10)
    print(f"Parent: I am the parent process")
    print(f"Parent: Parent's PID: {os.getpid()}")

    for i in range(num_children):
        print("-" * 5)
        print(f"Starting Process {i}")

        # forking a new process
        Process(target=run_child).start()

def main():
    num_children = 3
    start_parent(num_children)


if __name__ == "__main__":
    main()
