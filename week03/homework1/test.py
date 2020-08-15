import time
from multiprocessing import Process, freeze_support


def run():
    print("Start child process")
    time.sleep(2)
    print("End child process")


if __name__ == "__main__":
    freeze_support()
    print("Start parent process")
    p = Process(target=run)
    p.start()
    print("End parent process")
