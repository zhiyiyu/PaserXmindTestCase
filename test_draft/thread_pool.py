# coding: UTF-8

import time

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED


# 定义一个任务
def task(name):
    print(f"Task {name} started.")
    time.sleep(2)
    print(f"Task {name} completed.")
    return f"Task {name} result"


# 创建线程池
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    futures = [executor.submit(task, i) for i in range(5)]

    # 等待第一个任务完成或超时（5秒）
    done, not_done = wait(futures, timeout=5, return_when=FIRST_COMPLETED)

    # 处理完成的任务
    for future in done:
        result = future.result()
        print(result)

    # 取消未完成的任务
    for future in not_done:
        future.cancel()
