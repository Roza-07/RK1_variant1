"""Задание 2: исправление гонки потоков при помощи Lock."""

import threading

counter = 0
lock = threading.Lock()


def worker() -> None:
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1


if __name__ == "__main__":
    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter)
