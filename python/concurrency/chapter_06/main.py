"""
An application is considered bound by something when the requried resource for its work is the bottleneck
for achieving insreased performance. There are two main types of operations: CPU-bound and I/O-bound.

CPU-bound:
    An application is bound by the CPU if it would run faster if the CPU was faster,
    it spends most of its time just using the CPU doing some kind of computation
    Some examples of CPU-bound operations:
        - Mathematical operations like addition, subtraction, division, matrix, multiplication, etc
        - Encryption and decryption algorithms involve a lot of computationally intensive operations like: prime factorization,
        computing cryptographic functions, etc
        - Image processing, video processing, etc
        - Executing algorithms like binary search, sorting, etc
I/O-bound:
    An application is bound by I/O if it would run faster if the I/O sybsystem was faster. You can imagine with 
    reading from disk or getting user input or waiting for network response.

    Examples of I/O-bound operations are:
        - GUI applications are I/O bound: most of time is waiting on user interaction via the keyboard or mouse
        - Doing disk I/O or network I/O like databases or web servers


"""
def main():
    print(f"{__name__} is executing...")


if __name__ == "__main__":
    main()
