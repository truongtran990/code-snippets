import time
import concurrent.futures

def do_stuff(seconds=1):
    print(f"starting do_stuff that takes {seconds} second(s)")

    time.sleep(seconds)

    return (f"completed do_stuff")


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        do_stuff_executions = [executor.submit(do_stuff, i) for i in range(10)]
        
        for stuff in concurrent.futures.as_completed(do_stuff_executions):
            result = stuff.result()
            print(result)


if __name__ == "__main__":
    start_time = time.perf_counter()
    
    main()
    
    finish_time = time.perf_counter()
    print(f"Finished in {round(finish_time - start_time, 4)} in second(s)")
