import threading
import time


class MyThreadPool(threading.Thread):
    """
    Custom thread with delay in seconds.
    """
    def __init__(self, target, args, delay):
        super().__init__(target=target, args=args)
        self.delay = delay

    def run(self):
        time.sleep(self.delay)
        super().run()


def printer(a):
    print(f"Hello {a}")
    print(f"Thread {a} is working...")
    print(f"Bye {a}")


thread1 = MyThreadPool(target=printer, args=('1', ), delay=3)
thread2 = MyThreadPool(target=printer, args=('2', ), delay=1)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
