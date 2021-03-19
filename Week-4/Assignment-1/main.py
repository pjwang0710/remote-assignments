import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

def main():
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=do_job, args=(i, )))
    for thread in threads:
        thread.start()

main()