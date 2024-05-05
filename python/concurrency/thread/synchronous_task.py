import time

def do_stuff(seconds=1):
    print(f"starting do_stuff that takes {seconds} second(s)")

    time.sleep(seconds)

    print(f"completed do_stuff")

def main():
    for i in range(10):
        do_stuff(i)

if __name__ == "__main__":
    start_time = time.perf_counter()
    
    main()
    
    finish_time = time.perf_counter()
    print(f"Finished in {round(finish_time - start_time, 4)} in second(s)")
