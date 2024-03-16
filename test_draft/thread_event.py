# coding: UTF-8


import threading


class MyThread(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        print("线程{}已初始化完成，随时准备启动....".format(self.name))
        # 设置线程等待
        self.event.wait()
        print("{}开始执行...".format(self.name))


if __name__ == '__main__':
    event = threading.Event()
    threads = []
    [threads.append(MyThread(event)) for i in range(1, 11)]
    # 必须在子线程start之前先清空所有的event设置，让子线程的event.wait生效
    event.clear()
    [t.start() for t in threads]
    # 设置event事件，事件设置后将通知所有设置了事件对象的线程激活
    event.set()
    [t.join() for t in threads]
